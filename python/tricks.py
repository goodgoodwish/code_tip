

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

