# Two pointers algorithm,

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        if head is None:
            return 
        if head.next is None or head.next.next is None:
            return head
        mid = head
        fast = head
        while fast.next.next:
            mid = mid.next
            fast = fast.next.next 
            if fast.next is None:
                break
        return mid

class TwoSum:
    def __init__(self,):
        self.nums = []
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        self.nums.append(number)
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        unique_nums = set()
        for first in self.nums:
            second = value - first 
            if second in unique_nums:
                return True 
            unique_nums.add(first)
        return False

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # left, right pointer, and zone condition
        if nums is None or len(nums) == 0:
            return nums
        zero = 0
        one = 0
        nums_len = len(nums) - 1
        while one <= nums_len and zero <= nums_len:
            if nums[zero] != 0:
                zero += 1
                one += 1
            elif nums[one] == 0:
                one += 1
            elif nums[one] != 0:
                nums[zero], nums[one] = nums[one], nums[zero]
                one += 1
                zero += 1
        return nums

test = Solution()
r = test.moveZeroes([0,1,0,3,12])
print(r)
r = test.moveZeroes([-1,2,-3,4,0,1,0,-2,0,0,1])
print(r)
r = test.moveZeroes([-1,2,-3,4,1])
print(r)

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        i1 = 1
        i2 = 1
        end = len(nums) - 1
        while i2 <= end and i1 <= end:
            if nums[i1] > nums[i1 - 1]:
                i1 += 1
                i2 += 1
            elif nums[i2] == nums[i1 - 1]:
                i2 += 1
            elif nums[i2] > nums[i1 - 1]:
                nums[i1], nums[i2] = nums[i2], nums[i1]
                i2 += 1
                i1 += 1
        return i1

test = Solution()
r = test.deduplication([1,3,1,4,4,2])
print(r)

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        if len(nums) <= 1:
            return len(nums)
        A = set()
        for n in nums:
            A.add(n)
        i = 0
        for n in A:
            nums[i] = n
            i += 1
        print(nums)
        return len(A)

test = Solution()
r = test.deduplication([1,3,1,4,4,2])
print(r)

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        if nums is None:
            return 
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] == target:
                return [left + 1, right + 1]

test = Solution()
r = test.twoSum([1,3,4,4,9], 8)
print(r)

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        if nums is None:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left <= right and nums[right] >= k:
                right -= 1
            while left <= right and nums[left] < k:
                left += 1
            if left <= right:
                nums[right], nums[left] = nums[left], nums[right]
                right -= 1
                left += 1
        return left

test = Solution()
r = test.partitionArray([4,1,2,2,5], 2)
print(r)

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if numbers is None or len(numbers) <= 2:
            return
        numbers.sort()
        A = numbers
        ret = []
        i1 = 0
        end = len(A) - 1
        for i1 in range(end - 1):
            if i1 > 0 and A[i1] == A[i1 - 1]:
                continue
            left = i1 + 1
            right = end
            while left < right:
                if left >= i1 + 2 and A[left] == A[left - 1]:
                    left += 1
                    continue 
                elif A[i1] + A[left] + A[right] == 0:
                    ret.append([A[i1], A[left], A[right]])
                    left += 1
                elif A[i1] + A[left] + A[right] > 0:
                    right -= 1
                elif A[i1] + A[left] + A[right] < 0:
                    left += 1
        return ret

test = Solution()
r = test.threeSum([-1, 0, 1, 2, -1, -4, -3, 1, 2])
print(r)
