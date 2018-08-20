class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return -1
        start = 0
        end = len(A) - 1
        right_high = A[end]
        return self.r_search(A, target, 0, end, right_high)
    def r_search(self, A, target, start, end, right_high):
        while start + 1 < end:
            mid = start + (end - start)//2
            print(mid, A[mid])
            if A[mid] == target:
                print(mid, A[mid])
                return mid
            elif A[mid] < right_high and target > right_high:
                end = mid
            elif A[mid] > right_high and target <= right_high:
                start = mid
            elif A[mid] < target:
                start = mid
            elif A[mid] > target:
                end = mid
        if A[start] == target:
            return start 
        elif A[end] == target:
            return end
        return -1

test = Solution()
test.search([4, 5, 1, 2, 3], 1)
test.search([4, 5, 1, 2, 3], 2)
test.search([4, 5, 6, 7, 1, 2, 3], 9)
test.search([4, 5, 6, 7, 1], 1)

test.search([1, 2, 3], 1)
