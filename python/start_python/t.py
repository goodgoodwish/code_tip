class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        if abs(x) > 1 and n < -100:
            return 0
        n_half = abs(n) // 2
        if n % 2 == 1 and n > 0:
            base = x * self.myPow(x, n_half) * self.myPow(x, n_half)
        elif n > 0:
            base = self.myPow(x, n_half) * self.myPow(x, n_half)
        elif abs(n) % 2 == 1 and n < 0:
            base = 1/x * self.myPow(x, -n_half) * self.myPow(x, -n_half)
        elif n < 0:
            base = self.myPow(x, -n_half) * self.myPow(x, -n_half)
        return base

test = Solution()
test.myPow(2, 2)
test.myPow(2, 3)
test.myPow(34.00515, -3)
test.myPow(2.0, -2147483648)

class Parent:
    def __init__(self, name):
        self.father, self.mother = None, None
        self.name = name

p = Parent("z3")
p.father = Parent("z2")
p.mother = Parent("l2")
p.father.father = Parent("z1")

def find_parents(person, parents):
    if person.father is not None:
        p = person.father
        parents.append(p.name)
        find_parents(p, parents) 
    if person.mother is not None:
        p = person.mother
        parents.append(p.name)
        find_parents(p, parents) 
    return parents

find_parents(p, [])
