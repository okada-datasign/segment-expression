import func

OPERATOR = 'operator'
FUNC = 'func'
REF = 'ref'
LITERAL = 'literal'
ARGS = 'args'

operator_symbols = {
    'and': 'and',
    'or': 'or',
    'eq': '==',
    'not': 'not',
    'gt': '>',
    'lt': '<',
    'gte': '<=',
    'lte': '>=',
}


def compile(exp_tree: dict) -> str:
    if OPERATOR in exp_tree:
        op = exp_tree[OPERATOR]
        args = exp_tree[ARGS]
        compiled_args = [compile(arg) for arg in args]
        return '_{}({})'.format(op, ', '.join(compiled_args))
    elif FUNC in exp_tree:
        func = exp_tree[FUNC]
        args = exp_tree[ARGS]
        compiled_args = [compile(arg) for arg in args]
        return '_{}({})'.format(func, ', '.join(compiled_args))
    elif REF in exp_tree:
        ref = exp_tree[REF]
        tokens = ref.split('.')
        ref = tokens[0]
        if len(tokens) > 1:
            ref += "['" + "']['".join(tokens[1:]) + "']"
        return ref
    elif LITERAL in exp_tree:
        literal = exp_tree[LITERAL]
        if isinstance(literal, str):
            return "'{}'".format(literal)
        else:
            return str(literal)
    else:
        raise Exception('InvalidSegmentExpressionSyntax')


def compiles(exp_tree: dict, operators: dict = operator_symbols) -> str:
    if OPERATOR in exp_tree:
        op = exp_tree[OPERATOR]
        args = exp_tree[ARGS]
        compiled_args = [compiles(arg) for arg in args]
        return '(' + (' {} '.format(operators[op])).join(compiled_args) + ')'
    elif FUNC in exp_tree:
        func = exp_tree[FUNC]
        args = exp_tree[ARGS]
        compiled_args = [compiles(arg) for arg in args]
        return '{}({})'.format(func, ', '.join(compiled_args))
    elif REF in exp_tree:
        ref = exp_tree[REF]
        return ref
    elif LITERAL in exp_tree:
        literal = exp_tree[LITERAL]
        if isinstance(literal, str):
            return "'{}'".format(literal)
        else:
            return str(literal)
    else:
        raise Exception('InvalidSegmentExpressionSyntax')


def evaluate(exp_tree: dict, variables: dict) -> bool:
    g = {}
    g['locals'] = None
    g['globals'] = None
    g['__name__'] = None
    g['__file__'] = None
    g['__builtins__'] = None

    context = {
        '_and': func._and,
        '_or': func._or,
        '_eq': func._eq,
        '_not': func._not,
        '_gt': func._gt,
        '_lt': func._lt,
        '_gte': func._gte,
        '_lte': func._lte,
        '_count': func._count,
        '_sum': func._sum,
        '_max': func._max,
        '_min': func._min,
        '_distinct': func._distinct,
        '_has': func._has,
        '_fileter': func._fileter,
        '_select': func._select,
    }

    context.update(variables)
    expression = compile(exp_tree)
    return eval(expression, g, context)
