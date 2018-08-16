class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return
        start = 0
        end = len(A) - 1
        self.quick_sort(A, start, end)
        print(A)
    def quick_sort(self, A, start, end):
        if start >= end:
            return
        left = start
        right = end
        mid = int((start + end)/2)
        pivot = A[mid]
        while (left <= right):
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        self.quick_sort(A, start, right)
        self.quick_sort(A, left, end)

test = Solution()
test.sortIntegers2([1,4,2,7,8,5,3])
