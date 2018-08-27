import collections

class MyIter:
    def __init__(self,):
        self.q = collections.deque()
        self.generator01 = self.inorder_gen()
        # iterator01 = generator01.__iter__()
    def inorder_gen(self,):
        yield 1
        yield 2
    def next(self,):
        if self.has_next():
            next_value = self.q.popleft()
            return next_value
    def has_next(self,):
        if len(self.q) > 0:
            return True
        try:
            next_value = next(self.generator01) # or, iterator01.__next__()
            print("next val:", next_value)
            self.q.append(next_value)
            return True
        except StopIteration:
            return False

iter1 = MyIter()
iter1.has_next() # True
iter1.next() # 1
iter1.next() # 2
iter1.has_next() # False
iter1.next() # nothing
iter1.has_next() # False
