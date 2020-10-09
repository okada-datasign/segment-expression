import yaml
from expression import compile, compiles, evaluate

user_attributes = {
    'first_name': 'foo',
    'last_name': 'bar',
    'gender': 'Cis Female',
    'age': 40,
}

bank = [
    {
        'name': 'MUFJ',
        'branch': 'Shibuya',
        'amount': 1000000,
    },
    {
        'name': 'MIZUHO',
        'branch': 'Shinjuku',
        'amount': 2000000,
    },
]

date_of_births = [
    {
        'relationship': '子供',
        'branch': '2010-01-01',
    },
    {
        'relationship': '子供',
        'branch': '2012-10-10',
    },
]

hobbies = ['読書', 'ドライブ', 'スポーツ', 'スポーツ観戦', 'アウトドア']


variables = {
    'user_attributes': user_attributes,
    'bank': bank,
    'date_of_births': date_of_births,
    'hobbies': hobbies,
}


with open('expression.yml') as yml:
    exp = yaml.safe_load(yml)

print('--------------------------------------------------')
print('The expression to display:')
print('--------------------------------------------------')
print(compiles(exp))
print()

print('--------------------------------------------------')
print('The expression to evaluate:')
print('--------------------------------------------------')
print(compile(exp))
print()

print('--------------------------------------------------')
print('Result:')
print('--------------------------------------------------')
print(evaluate(exp, variables))
