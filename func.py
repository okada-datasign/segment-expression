from typing import List
from statistics import mean


def _and(*args) -> bool:
    for arg in args:
        if not arg:
            return False
    return True


def _or(*args) -> bool:
    for arg in args:
        if arg:
            return True
    return False


def _eq(a, b) -> bool:
    return a == b


def _not(a) -> bool:
    return not a


def _gt(a, b) -> bool:
    return a > b


def _lt(a, b) -> bool:
    return a < b


def _gte(a, b) -> bool:
    return a >= b


def _lte(a, b) -> bool:
    return a <= b


def _count(records: List, field: str = '*'):
    return len(records if field == '*' else [r[field] for r in records])


def _sum(records: List, field: str = '*'):
    return sum(records if field == '*' else [r[field] for r in records])


def _avg(records: List, field: str = '*'):
    return mean(records if field == '*' else [r[field] for r in records])


def _max(records: List, field: str = '*'):
    return max(records if field == '*' else [r[field] for r in records])


def _min(records: List, field: str = '*'):
    return min(records if field == '*' else [r[field] for r in records])


def _distinct(records: List, field: str = '*'):
    return set(records if field == '*' else [r[field] for r in records])


def _has(records: List, v) -> bool:
    return v in records


def _fileter(records: List) -> List:
    pass


def _select(records: List, field: str) -> List:
    return [r[field] for r in records]
