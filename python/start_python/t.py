class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if A is None or len(A) == 0:
            return -1
        start = 0
        end = len(A) - 1
        k_value = self.quick_select(k, A, start, end)
        print(A, k_value)
        return k_value
    def quick_select(self, k, A, start, end):
        if start >= end:
            if start == k - 1:
                print("1st", start, A[start])
                return A[start]
        mid = int((start + end)/2)
        pivot = A[mid]
        print("pivot: ", pivot)
        left = start 
        right = end 
        while left <= right:
            while left <= right and A[left] > pivot:
                left += 1
            while left <= right and A[right] < pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        print(A, right)
        if k - 1 <= right and k - 1 >= start:
            return self.quick_select(k, A, start, right)
        elif k - 1 >= left and k - 1 <= end:
            return self.quick_select(k, A, left, end)
        elif k - 1 == right + 1:
            print("2nd, ", k - 1, A[k - 1])
            return A[k - 1]

test = Solution()
test.kthLargestElement(5, [8,4,7,1,6,5,7,2,3])
