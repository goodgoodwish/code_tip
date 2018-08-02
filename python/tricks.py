
2 Patterns for cleaner Python 

2.1 Covering your ass with Assertions - debugging aid, test bugs

assert_statement ::= "assert" test_condition [, error_message]

if __debug__:
    if not test_condition:
        raise AssertionError(error_message)

assert 0 <= price <= product["prince"]

2.2 Complacent comma placement

names = [
    "Zhang 3",
    "Li 4",
    "Wang 5",
]

2.3 Context managers and the with statement 

with open("hello.txt", "w") as f:
    f.write("Hellow, Yi. \n")

f = open("hello.txt", "w")
try:
    f.write("Hello, Yi. \n")
finally:
    f.close()

class ManageFile:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        self.file = open(self.name, "w")
        return self.file 
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManageFile("h1.txt") as f:
    f.write("Hi 1 \n")
    f.write("bye now. \n")

from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, "w")
        yield f 
    finally:
        f.close()

with managed_file("h2.txt") as f:
    f.write("Hi 2 \n")
    f.write("bye now. \n")

2.4 Underscore, dunder, and more

_var : intend for internal use.
var_ : break (keyword) naming conflict.
__var: name mangling, to rewrite attribute name to avoid naming conflicts in subclass.

class Test:
    def __init__(self):
        self.foo = 18
        self.__bazz = 7
    def get_mangled(self):
        return self.__bazz
    def __method(self):
        return 42
    def call_it(self):
        return self.__method()

t = Test()
dir(t)
['_Test__bazz', 'foo']
t.get_mangled()
7

t.__method()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Test' object has no attribute '__method'

t.call_it()
42

t._Test__bazz
7
t._Test__method()
42

__var__ : reserved for special use.
_ : a variable is temporary or insignificant.

car = ("red", "auto", 2005, 1812.5)
color, _, _, mileage = car

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

# date time
import datetime
week_ago = datetime.date.today() - datetime.timedelta(days=7) # return example: datetime.date(2018, 7, 20)
self.week_ago_str = "{:%Y-%m-%d}".format(week_ago) # example: 2018-07-20

2.6 The Zen of Python 

import this 

3. Effective functions 

3.1 Python function are first-class

def yell(text):
    return text.upper() + "!"

bark = yell 

# Function is object, can be stored in data structures

func_list = [bark, str.lower, str.capitalize]

for f in func_list:
    print(f("Hi there"), f)

HI THERE! <function yell at 0x10129be18>
hi there <method 'lower' of 'str' objects>
Hi there <method 'capitalize' of 'str' objects>

# Function can be passed to other functions

def greet(func_a):
    greeting = func_a("Hi, I like swimming.")
    print(greeting)

list(map(bark, ["hello", "hey", "hi"]))
['HELLO!', 'HEY!', 'HI!']

# Function can be nested
# Function can be returned from another function.

def get_speak_func(volume):
    def whisper(text):
        return text.lower() + "..."
    def yell(text):
        return text.upper() + "!"
    if volume > 0.5:
        return yell 
    else:
        return whisper

get_speak_func(0.8)("Watch for horse poo")
'WATCH FOR HORSE POO!'

# Function can capture local state. Closure.

def make_adder(base):
    def add(x):
        return base + x
    return add

plus_2 = make_adder(base=2)
plus_5 = make_adder(base=5)

plus_2(2) # 4
plus_5(5) # 10

# Object can behave like function

class Adder:
    def __init__(self, base):
        self.base = base 
    def __call__(self, x):
        return self.base + x 

plus_20 = Adder(20)
plus_20(2) # 22

3.2 Lambda is single-expression function

# implicit return expression result,
add = lambda x, y: x + y # Evaluate when access,
add(1, 7)

(lambda x, y: x + y)(1, 7) # Function expression

list( filter(lambda x: x[0] + x[1] > 4, [(1,2),(2,3),(3,4),(4,5)]) )
[(2, 3), (3, 4), (4, 5)]

3.3 Decorator

def null_decorator(func):
    def box():
        result = func()
        return result + ", Zhang 3."
    return box

@null_decorator
def greet():
    return "Hi"

# Decorator can modify behavior.
# multi decorator

def strong(func):
    def box():
        return "<strong>" + func() + "</strong>"
    return box 

def li(func):
    def box():
        return "<li>" + func() + "</li>"
    return box 

@li
@strong 
def greet():
    return "How are you?"

greet()
'<li><strong>How are you?</strong></li>'

# accept arguments
# forward arguments

def trace(func):
    def box(*args, **kwargs):
        print(f"LOG: {func.__name__}() start."
              f"with {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"LOG: {func.__name__}() end.")
        return result
    return box

@trace 
def greet(a,b,key,key2):
    return "How are you?"

greet("a","b",key="1",key2="2")

LOG: greet() start.with ('a', 'b'), {'key': '1', 'key2': '2'}
LOG: greet() end.
'How are you?'

# Debuggable decorators ,functools.wraps()
def greet():
    """return a friendly greeting."""
    return "How are you?"

greet.__doc__
'return a friendly greeting.'
greet.__name__
'greet'

import functools

def upper_case(func):
    @functools.wraps(func) # <<<
    def wrapper():
        result = func().upper()
        return result
    return wrapper

@upper_case
def greet():
    """return a friendly greeting."""
    return "How are you?"

greet.__doc__
'return a friendly greeting.'
greet.__name__
'greet'

3.4 Fun with *args and **kwargs

def foo(required_arg, *args, **kwargs):
    print(required_arg)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

foo("abc-required", 1, 2, key1="value_1", key2 = "v2")

abc-required
(1, 2)
{'key1': 'value_1', 'key2': 'v2'}

class Car:
    def __init__(self, color, wheel):
        self.color = color
        self.wheel = wheel 

class AlwaysRedCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = "red"

AlwaysRedCar("green", 4).color
'red'
AlwaysRedCar("green", wheel=8).wheel
8

3.5 Function argument unpacking

3.6 Nothing to return here


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
