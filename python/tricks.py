
2 Patterns for cleaner Python 

2.1 Covering your ass with Assertions 

2.2 Complacent comma placement

# 2.5 String formatting,

my_name = 'Jusling'
my_id = 101
s1 = 'Hey %(name)s, %(id)i ' % {"name": my_name, "id": my_id}

s1n = 'Hello, {}'.format(my_name)
s1n1 = 'Hello, {}, {}'.format(my_name, my_id)  # positional formatting 
s2n = 'Hello, {name}, {id}'.format(name=my_name, id=my_id) # substitution by name

# Literal string interpolation, python 3.6+ 
s1i = f'Hello, {my_name}, you are {my_id} '

print(s1n)
print(s2n)

for i in range(3):
    print(i)

list(filter(lambda x: x>1, range(3)))  # Lambda
[x for x in range(4) if x > 1]  # list comprehension, or generator expression 

# type hints

def foo(a: str, b: int) -> str:
  ms: str = a + str(b)
  print(a, b)
  return ms 
  

foo("25", 78)

# 4 Class and OOP

# 4.7 Class vs instance variable

class Noodle:
    ingredient = "flour"
    name = "Noodle"
    count = 0
    def __init__(self, name):
        self.name = name
        self.count = 0
    def eat(self):
        self.__class__.count += 1
        self.count += 2
        print("instance name: ", self.name)
        print("class name: ", self.__class__.name)
        print("class var, ingr: ", self.__class__.ingredient)
        print("instance var, count: ", self.count)
        print("class var, count: ", self.__class__.count)

qi_shan = Noodle("qi_shan")
qi_shan.eat()

# 5 Common data structures

# 5.1 

phone_book = {
    "bob": 1002,
    "alice": 1003,
    "jusling": 1004,
}

squares = {x: x*x for x in range(4)}

{0: 0, 1: 1, 2: 4, 3: 9}

import collections 

d = collections.OrderedDict(one=1, two=2, three=3)
d["four"] = 4
d.keys()
odict_keys(['one', 'two', 'three', 'four'])

from collections import defaultdict
dd = defaultdict(list)
dd["dogs"].append("Rufus")
dd["dogs"].append("Juliet")
dd["dogs"]

from collections import ChainMap
dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain = ChainMap(dict1, dict2)

chain
ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})

# ChainMap searches each collection in the chain
# from left to right until it finds the key (or fails):
chain['three']
3
chain['one']
1
chain['ten']
KeyError: 'ten'

# 6 Looping and Iteration

list(range(0, 10, 2))

for i in range(0, 10, 2):
    print(i)

0
2
4
6
8

my_itmes = ["A","B","C"]

for item in my_itmes:
    print(item)

for i, item in enumerate(my_itmes):
    print(f"{i}: {item}")

emails = {
    "Bob": "bob@abc.com",
    "Alice": "alice@abc.com",
}

for name, email in emails.items():
    print(f"{name} -> {email}" )

7. 

7.1 Dictionary default values

id_name = {
    58: "Linton",
    92: "Tom",
    21: "Drewsling"
}

def greeting(user_id):
    if user_id in id_name:
        return f"Hi {id_name[user_id]} ! "
    else:
        return "Hi friend."

    """easier to ask for forgiveness than permission, EAFP"""
    try:
        return f"Hi {id_name[user_id]} ! "
    except KeyError:
        return "Hi friend."

user_id=18
"Hi %s!" % id_name.get(user_id, "friend")

user_id=21
f"""Hi {id_name.get(user_id, "friend")}"""

7.2 Sorting Dictionary for fun

xs = {
    "b": 3,
    "c": 4,
    "a": 2,
    "d": 1,
}

sorted(xs.items())
[('a', 2), ('b', 3), ('c', 4), ('d', 1)]

sorted(xs.items(), key=lambda x: x[1])
sorted(xs.items(), key=lambda x: x[1])
[('d', 1), ('a', 2), ('b', 3), ('c', 4)]

# using itemgetter() to retrieve specific fields,

import operator
sorted(xs.items(), key=operator.itemgetter(1))
[('d', 1), ('a', 2), ('b', 3), ('c', 4)]
sorted(xs.items(), key=operator.itemgetter(0))
[('a', 2), ('b', 3), ('c', 4), ('d', 1)]
sorted(xs.items(), key=operator.itemgetter(0), reverse=True)
[('d', 1), ('c', 4), ('b', 3), ('a', 2)]

7.3 Emulating Switch/Case statement with Dict, and function variable

def my_func_1(a, b):
    return a + b 

def my_func_2(a, b):
    return a * b

def my_func_other(a, b):
    return max(a, b)

my_functions = [my_func_1, my_func_2]

my_functions[0](3,5)
8

function_dict = {
    "plus": my_func_1,
    "multi": my_func_2,
}

function_dict["multi"](3,5)
15

def dispatch_dict(operator, x, y):
    return function_dict.get(operator, my_func_other)(x, y)

dispatch_dict("unknow", 7, 8)
8
dispatch_dict("plus", 7, 8)
15

7.4 The craziest dict expression,

>>> {True: "yes", 1: "no", 1.0: "maybe"}

{True: 'maybe'}

>>> True == 1 == 1.0
True

xs = dict()
xs[True] = 'yes'
xs[1] = 'no'
xs[1.0] = 'maybe'

["no", "yes"][True] # "yes" ,  True == 1.

class AlwaysEqual:
    def __eq__(self, other):
        return True
    def __hash__(self):
        return id(self)

AlwaysEqual() == 28 # True

a = AlwaysEqual()
b = AlwaysEqual()

hash(a), hash(b) # (4390785152, 4390785264)

7.5 Many ways to merge Dictionary

xs = {"a": 1, "b": 2}
ys = {"c": 3, "d": 4}

zs = {}
zs.update(xs)
zs.update(ys)

zs
{'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Python 3.5
zs = {**xs, **ys}

{'a': 1, 'b': 2, 'c': 3, 'd': 4}

7.6 Dictionary pretty printing

zs = {'a': 1, 'b': 2, 'c': 0xc0ffee, 'd': 4}
str(zs)

import json
json.dumps(zs, indent=4, sort_keys=True)

zs["e"] = {1,2,3}

import pprint
pprint.pprint(zs)
{'a': 1, 'b': 2, 'c': 12648430, 'd': 4, 'e': {1, 2, 3}}

8 Pythonic productivity techniques

8.1 Exploring Python modules and objects

import datetime 
dir(datetime)

dir(datetime.date)

[x for x in dir(datetime) if "date" in x.lower()]
['date', 'datetime', 'datetime_CAPI']

help(datetime.date)

8.2 Isolating project dependencies with virtualenv

cd ~/app/python
python -m venv ./env1

source ./env1/bin/activate

which pip 
which python 
pip list 

pip install schedule 
pip list 

deactivate

find ./ -name requirements.txt

.//git/bi-cloud/etl/requirements.txt

8.3 Peeking behind the Bytecode curtain

def greet(name):
    return "Hi, " + name + "!_!"

greet.__code__.co_code
greet.__code__.co_varnames
greet.__code__.co_consts

import dis
dis.dis(greet)

  2           0 LOAD_CONST               1 ('Hi, ')
              2 LOAD_FAST                0 (name)
              4 BINARY_ADD
              6 LOAD_CONST               2 ('!_!')
              8 BINARY_ADD
             10 RETURN_VALUE
