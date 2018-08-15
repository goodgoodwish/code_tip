class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        new_arr = []
        start = 0
        end = len(A) - 1
        target_pos = 0
        top = 1
        left = 1
        right = 1
        while start + 1 < end:
            mid = int(start + (end - start)/2)
            if A[mid] == target:
                target_pos = mid
                break
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[mid] == target:
            pass
        elif abs(A[start] - target) < abs(A[end] - target):
            target_pos = start
        else:
            target_pos = end
        new_arr.append(A[target_pos])
        print(target_pos)
        for i in range(k - 1):
            print(left, right, i)
            if left > target_pos:
                new_arr.append(A[target_pos + right])
                right += 1
            elif right + target_pos > len(A) - 1:
                new_arr.append(A[target_pos - left])
                left += 1
            elif abs(A[target_pos - left]) <= abs(A[target_pos + right]):
                new_arr.append(A[target_pos - left])
                left += 1
            else:
                new_arr.append(A[target_pos + right])
                right += 1
        return new_arr

test = Solution()
test.kClosestNumbers(A = [1, 4, 6, 8, 9, 12], target = 3, k = 3)
test.kClosestNumbers(A = [1, 2, 3], target = 2, k = 3)
test.kClosestNumbers(A = [1,4,6,10,20], target = 21, k = 4)
