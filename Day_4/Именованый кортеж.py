from collections import namedtuple

rec = namedtuple('rec', ['name', 'age', 'jobs'])
bob = rec('bob', age=40, jobs=['designer', 'manager'])
print(bob)
# rec(name='bob', age=40, jobs=['designer', 'manager'])

print(bob[0], bob[2])
# bob ['designer', 'manager']

print(bob.name, bob.age)
# bob 40

# Преобразование в словарь
g = bob._asdict()
print(f"{g},\nname: {g['name']}, jobs: {g['jobs']}")
# {'name': 'bob', 'age': 40, 'jobs': ['designer', 'manager']},
# name: bob, jobs: ['designer', 'manager']

