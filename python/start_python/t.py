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

start = "a"
end = "c"
dict = ["a","b","c"]

test = Solution()
r = test.findLadders(start, end, dict)
print(r)

# https://lintcode.com/problem/count-of-smaller-number-before-itself/description

class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def lowbit(self, v):
        # 10100, return 100,
        low_bit_value = v & (-v)
        return low_bit_value
    def modify(self, bit, index, delta_val):
        while (index < len(bit)):
            bit[index] += delta_val
            index += self.lowbit(index)
    def query(self, bit, index):
        prefix_sum = 0
        while index > 0:
            prefix_sum += bit[index]
            index -= self.lowbit(index)
        return prefix_sum
    def countOfSmallerNumberII(self, A):
        if not A:
            return []
        len_a = len(A)
        bit = [0 for i in range(len_a + 1)]
        value_index = {}
        result = []
        sorted_A = sorted(A)
        for i in range(len_a):
            value_index[sorted_A[i]] = i + 1 
        for i in range(len_a):
            self.modify(bit, value_index[A[i]], 1)
            result.append(self.query(bit, value_index[A[i]] - 1) )
        return result

test = Solution()
r = test.countOfSmallerNumberII([1,2,7,8,5])
print(r)

