

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

7.2 Sorting Dictionary for fun

7.3 Emulating Switch/Case statement with Dict 

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