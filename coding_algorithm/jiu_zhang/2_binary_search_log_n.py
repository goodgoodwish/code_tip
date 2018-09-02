# Binary Search and LogN algorithm

class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # find range
        base = 2
        start = 0
        while target > reader.get(base):
            base *= 2
        if reader.get(base) == 2147483647:
            return -1
        # search it in range
        start = (base - 1) // 2
        end = base
        while start + 1 < end:
            mid = start + (end - start)//2
            if reader.get(mid) == target:
                end = mid 
            elif reader.get(mid) < target:
                start = mid 
            elif reader.get(mid) > target:
                end = mid
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1


test = Solution()
l = test.searchBigSortedArray([1,3,6,9,21],30)
print(l)

class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        start = 1
        end = n
        while start + 1 < end:
            mid = start + (end - start)//2
            if SVNRepo.isBadVersion(mid):
                end = mid 
            elif SVNRepo.isBadVersion(mid) == False:
                start = mid + 1
        if SVNRepo.isBadVersion(start):
            return start 
        if SVNRepo.isBadVersion(end):
            return end

test = Solution()
l = test.findFirstBadVersion([1,3,6,9,21],30)
print(l)

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start)//2
            # print(mid, ": ", A[mid])
            if A[mid - 1] < A[mid] > A[mid + 1]:
                end = mid
            elif A[mid - 1] < A[mid] < A[mid + 1]:
                start = mid
            elif A[mid - 1] > A[mid] > A[mid + 1]:
                end = mid
            elif A[mid - 1] > A[mid] < A[mid + 1]: # valley point,
                end = mid
            else:
                end = mid 
        if A[start - 1] < A[start] > A[start + 1]:
            return start
        elif A[end - 1] < A[end] > A[end + 1]:
            return end

test = Solution()
l = test.findPeak([10,12,14,8,7,9,11,4,3])
print(l)

class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # double Multiplier
        c = a % b
        base = c
        if n == 0:
            return 1 % b
        result = 1
        while n > 0:
            if n % 2 == 1:
                result = (result * base) % b 
            base = (base * base) % b 
            n = n // 2 # n = n >> 1
            print(n)
        return result

test = Solution()
l = test.fastPower(3,7,5)
print(l)
l = test.fastPower(31,1,0)
print(l)


