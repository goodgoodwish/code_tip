class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        min_sum = 0
        max_sum = -float("inf")
        sum = 0
        start = 0
        end = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            max_sum = max(sum, max_sum)
            min_sum = min(sum, min_sum)
            if sum == min_sum:
                start = i + 1
            if sum == max_sum:
                end = i + 1 
        return nums[start:end]

test = Solution()
r = test.maxSubArray([-2,2,-3,4,-1,2,1,-5,3])
print(r)


# https://lintcode.com/problem/count-of-smaller-number-before-itself 

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


# https://lintcode.com/problem/count-of-smaller-numbers-after-self

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
    def countSmaller(self, A):
        if not A:
            return []
        len_a = len(A)
        bit = [0 for i in range(len_a + 1)]
        value_index = {}
        result = []
        A.reverse()
        sorted_A = sorted(A)
        for i in range(len_a):
            value_index[sorted_A[i]] = i + 1 
        for i in range(len_a):
            self.modify(bit, value_index[A[i]], 1)
            result.append(self.query(bit, value_index[A[i]] - 1) )
        result.reverse()
        return result

test = Solution()
r = test.countSmaller([1,2,7,8,5])
print(r)

class Solution:
    """
    idea: 
    * value based Binary search to find mid value.
    * index base Binary search to find count, values <= pivot,
    * 二分值，找个数；二分索引，找最后小于等于一个值的索引。

    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        half = (len(A) + len(B)) // 2
        if (len(A) + len(B)) % 2 == 0:
            return (self.find_kth(A, B, half) + self.find_kth(A, B, half + 1))/2
        else:
            return self.find_kth(A, B, half + 1)
    def find_kth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        start = min(A[0], B[0])
        end = max(A[- 1], B[- 1])
        print("K:", k)
        while start + 1 < end:
            mid = start + (end - start)//2
            front_count = self.front_count(A, B, mid)
            print(f"front count {front_count}, start,mid,end:", start,mid,end)
            if front_count == k:
                end = mid 
            elif front_count < k:
                start = mid 
            else:
                end = mid 
        pre_start_count = self.front_count(A, B, start)
        print(f"Final: pre start count {pre_start_count}, start,mid,end:", start,mid,end)
        if self.front_count(A, B, start) == k:
            return start
        return end
    def front_count(self, A, B, pivot):
        return self.count_items(A, pivot) + self.count_items(B, pivot)
    def count_items(self, A, pivot):
        # less than, and equal, inclusive,
        if A[-1] <= pivot:
            return len(A)
        if A[0] > pivot:
            return 0
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            if A[mid] == pivot:
                start = mid 
            elif A[mid] < pivot:
                start = mid 
            elif A[mid] > pivot:
                end = mid 
        print("binary search, start, end", start, end)
        print(f"{A[start]} - {pivot} - {A[end]}")
        if A[start] == pivot:
            return start + 1
        elif A[start] < pivot < A[end]:
            return start + 1
        elif A[end] == pivot:
            return end + 1

test = Solution()
# r = test.count_items([5,6,7,8,9], 10)
# print(r)
# r = test.findMedianSortedArrays([1,3,5,7],[2,4,6,8])
# print(r)
# r = test.findMedianSortedArrays([],[2])
# print(r)
# r = test.findMedianSortedArrays([1,2,3,4],[5,6,7,8,9])
# print(r)
r = test.findMedianSortedArrays([1],[70,99])
print(r)

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices:
            return 0
        min_price = float("inf")
        max_gain = 0
        for price in prices:
            min_price = min(min_price, price)
            max_gain = max(max_gain, price - min_price)
        return max_gain

test = Solution()
r = test.maxProfit([3,2,3,1,2])
print(r)

# https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iii 

class Solution:
    """
    最多交易两次。买进两次，卖出两次。

    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices:
            return 0
        size = len(prices)
        max_gain_left = [None] * size
        max_gain_right = max_gain_left[:]
        min_price = float("inf")
        max_gain = -float("inf")
        for i, price in enumerate(prices):
            min_price = min(min_price, price)
            max_gain = max(max_gain, price - min_price)
            max_gain_left[i] = max_gain
        max_gain = -float("inf") 
        max_price = -float("inf")
        for i in range(size - 1, -1, -1):
            max_price = max(max_price, prices[i])
            max_gain = max(max_gain, max_price - prices[i])
            print(i, max_price, prices[i], max_gain)
            max_gain_right[i] = max_gain
        print(max_gain_left, max_gain_right)
        max_gain = -float("inf")
        for i in range(size):
            max_gain = max(max_gain, max_gain_left[i] + max_gain_right[i])
        return max_gain

test = Solution()
r = test.maxProfit([4,4,6,1,1,4,2,5])
print(r)
r = test.maxProfit([1, 5])
print(r)

# https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-ii

class Solution:
    """
    constraint: many transactions.
    
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices or len(prices) == 1:
            return 0
        tot_gain = 0
        unique_prices = []
        pre_price = prices[0]
        unique_prices.append(pre_price)
        for price in prices:
            if price != pre_price:
                unique_prices.append(price)
            pre_price = price
        prices = unique_prices
        size = len(prices)
        if size <= 2:
            if prices[1] > prices[0]:
                return prices[1] - prices[0]
            else:
                return 0
        peak_index, low_index = -1, -1
        pre = 0
        for i in range(size):
            if ((i == 0 and prices[i] < prices[i + 1]) 
              or (i > 0 and i < size - 1 and prices[i - 1] > prices[i] < prices[i + 1])):
                low_price = prices[i]
                low_index = i
            if ((i == size - 1 and prices[i] > prices[i - 1])
              or (i > 0 and i < size - 1 and prices[i - 1] < prices[i] > prices[i + 1])):
                peak_price = prices[i]
                peak_index = i
            if peak_index > low_index > -1:
                tot_gain += peak_price - low_price
                peak_index, low_index = -1, -1
        return tot_gain

test = Solution()
r = test.maxProfit([2,1,2,0,1])
print(r)
r = test.maxProfit([1, 2, 5])
print(r)
r = test.maxProfit([3,3,5,0,0,3,1,4])
print(r)

lc, https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-with-transaction-fee 

class Solution:
    """
    @param prices: a list of integers
    @param fee: a integer
    @return: return a integer
    """
    def maxProfit(self, prices, fee):
        # write your code here
        if not prices or len(prices) == 1:
            return 0
        tot_gain = 0
        size = len(prices)
        buy = - prices[0]
        sell = 0
        for i in range(size):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i] - fee)
        return sell

test = Solution()
r = test.maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2)
print(r)

# 6 - 1 - 2,  not  (4 - 1 - 2) + (6 - 3 - 2)
# 4 - 3 = 1, 1 < 2, 收益小于交易费.
# 看看 模拟法 怎么处理.
r = test.maxProfit(prices = [1, 4, 3, 6], fee = 2)
print(r)

r = test.maxProfit(prices = [1, 4, 2, 5], fee = 2)
print(r)

lc, https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iv 

class Solution:
    """
    constraint: You may complete at most k transactions.

    @param prices: a list of integers
    @param k: trade k times,
    @return: return a integer
    """
    def maxProfit(self, k, prices):
        if not prices or len(prices) == 1:
            return 0
        buy = -prices[0]
        sell = 0
        if k > len(prices):
            for price in prices:
                buy = max(buy, sell - price)
                sell = max(sell, buy + price)
            return sell
        buys = [-float("inf")] * k
        sells = [0] * k
        for price in prices:
            buys[0] = max(buys[0], -price)
            for i in range(k):
                if i > 0:
                    buys[i] = max(buys[i], sells[i - 1] - price)
                sells[i] = max(sells[i], buys[i] + price)
        return sells[k - 1]

test = Solution()
r = test.maxProfit(prices = [1,3, 1, 4, 1, 5, 1, 6], k = 8)
print(r)


https://lintcode.com/problem/range-sum-query-mutable 

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
        if i > j:
            return 0
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

817. Range Sum Query 2D Mutable

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.bit = [[0 for _ in range(self.cols + 1)] for _ in range(self.rows + 1)]
        self.matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                self.update(r, c, matrix[r][c])
        
    def lowbit(self, x):
        return x & (-x)
    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        r = row + 1
        while r <= self.rows:
            c = col + 1
            while c <= self.cols:
                self.bit[r][c] += delta
                c += self.lowbit(c)
            r += self.lowbit(r)
    def getPrefixSum(self, row, col):
        r = row + 1
        sum = 0
        while r > 0:
            c = col + 1
            while c > 0:
                sum += self.bit[r][c]
                c -= self.lowbit(c)
            r -= self.lowbit(r)
        return sum
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = self.getPrefixSum(row2, col2)
        sum_upside = self.getPrefixSum(row1 - 1, col2)
        sum_leftside = self.getPrefixSum(row2, col1 - 1)
        sum_small = self.getPrefixSum(row1 - 1, col1 - 1)
        return sum - sum_upside - sum_leftside + sum_small
        
# https://www.lintcode.com/problem/range-sum-query-2d-mutable

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10

test = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
r = test.getPrefixSum(1, 1)
print(r)
r = test.getPrefixSum(2, 2)
print(r)
r = test.sumRegion(2, 1, 4, 3)
print(r)
# print(test.matrix)
# print(test.bit)
test.update(3, 2, 2)
r = test.sumRegion(2, 1, 4, 3)
print(r)

Range Sum Query 2D - Immutable

class NumMatrix:
    """
    @param: matrix: a 2D matrix
    """
    def __init__(self, matrix):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.matrix = [[0] * self.cols for _ in range(self.rows)]
        self.bit = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        for r in range(self.rows):
            for c in range(self.cols):
                self.update(r, c, matrix[r][c])

    def lowbit(self, x):
        return x & (-x)

    def update(self, row, col, value):
        delta = value - self.matrix[row][col]
        r = row + 1
        while r <= self.rows:
            c = col + 1
            while c <= self.cols:
                self.bit[r][c] += delta
                c += self.lowbit(c)
            r += self.lowbit(r)

    def prefix_sum(self, row, col):
        sum_val = 0
        r = row + 1
        while r > 0:
            c = col + 1
            while c > 0:
                sum_val += self.bit[r][c]
                c -= self.lowbit(c)
            r -= self.lowbit(r)
        return sum_val

    """
    @param: row1: An integer
    @param: col1: An integer
    @param: row2: An integer
    @param: col2: An integer
    @return: An integer
    """
    def sumRegion(self, row1, col1, row2, col2):
        sum_upside = self.prefix_sum(row1 - 1, col2)
        sum_leftside = self.prefix_sum(row2, col1 - 1)
        sum_small = self.prefix_sum(row1 - 1, col1 - 1)
        sum_big = self.prefix_sum(row2, col2)
        return sum_big - sum_leftside - sum_upside + sum_small
