class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        return []
    def find_next_words(self, word, dict):
        pass
    def bfs(self, start, end, dict, used):
        # from end to start
        steps2end = {}

    def dfs(self, start, end, dict, steps2end):
        pass

start = "a"
end = "c"
dict = ["a","b","c"]

test = Solution()
r = test.findLadders(start, end, dict)
print(r)

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        size = len(nums)
        self.nums = [0] * size
        self.bit = [0] * (size + 1)
        for i in range(size):
            self.update(i, nums[i])
        
    def lowbit(self, x):
        return x & (-x)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        end = len(self.nums)
        index = i + 1
        delta = val - self.nums[i]
        self.nums[i] = val
        while index <= end:
            self.bit[index] += delta
            index += self.lowbit(index)
    def prefix_sum(self, i):
        index = i + 1
        sum_value = 0
        while index > 0:
            sum_value += self.bit[index]
            index -= self.lowbit(index)
        return sum_value
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix_sum(j) - self.prefix_sum(i - 1)
        

obj = NumArray([0,9,5,7,3])
print(obj.bit)
print(obj.sumRange(0, 1))
print(obj.sumRange(0, 2))
print(obj.sumRange(1, 2))
print(obj.sumRange(4, 4))
print(obj.sumRange(2, 4))
print(obj.sumRange(3, 3))
obj.update(4, 5)
obj.update(1, 7)
obj.update(0, 8)
print(obj.sumRange(1, 2))
obj.update(1, 9)
print(obj.sumRange(4, 4))
obj.update(3, 4)
