https://www.lintcode.com/problem/longest-palindromic-substring/description

def longestPalindrome(s):
    def search(right_step):
        left_start = 0
        right_start = 0
        cur_half_len = 0
        min_half_len = 0
        max_pal = ""
        for i in range(len(s)-1):
            left_start = i 
            right_start = left_start + right_step
            if right_start >= len(s):
                break
            min_half_len = min(left_start + 1, len(s) - right_start)
            for j in range(min_half_len):
                print(j, s[left_start - j:left_start+1], s[left_start - j], s[right_start + j])
                if s[left_start - j] != s[right_start + j]:
                    # print(j, s[left_start - j:left_start+1], s[left_start - j], s[right_start + j])
                    cur_half_len = j - 1
                    print("cur_half_len:", cur_half_len)
                    break
                else:
                    cur_half_len = j
            # print("Max_len: ", cur_half_len, s[left_start - j:left_start], s[left_start - j], s[right_start + j])
            if cur_half_len + 1 > len(max_pal) / 2:
                max_pal = s[left_start - cur_half_len: right_start + cur_half_len + 1]
        print(f"It is: {max_pal}")
        return max_pal
    pal1 = search(1)
    pal2 = search(2)
    if len(pal1) > len(pal2):
        return pal1 
    else:
        return pal2

# longestPalindrome("abcddcab")
# longestPalindrome("abcdxdcab")
longestPalindrome("cbaabcu")
longestPalindrome("xucbaabcu")

class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        if s is None or s == "":
            return 0
        if len(s) <= 1:
            return 1
        char_cnt = {}
        max_len = 0
        for char in s:
            print(char)
            # if char in char_cnt:
            #     char_cnt[char] += 1
            # else:
            #     char_cnt[char] = 1
            char_cnt[char] = char_cnt.get(char,0) + 1
        for char, cnt in char_cnt.items():
            print(char, cnt)
            if cnt < 2:
                continue
            else:
                max_len = max_len + int(cnt/2)*2
        if len(s) > max_len:
            max_len += 1
        return max_len

test = Solution()
test.longestPalindrome("uvaabbcc")

Chapter 2, Binary search.

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer, last position that value = target
    """
    def lastPosition(self, nums, target):
        # write your code here
        start = 0
        end = len(nums) - 1
        arr_len = len(nums)
        while start <= end:
            mid = int((start + end)/2)
            if (nums[mid] == target):
                while mid < arr_len - 1 and nums[mid + 1] == target:
                    mid = mid + 1
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1

test = Solution()
test.lastPosition(nums = [1, 2, 2, 2, 4, 5, 5], target = 2)

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer, last position that value = target
    Goal: Binary search template, from JiuZhang
    """
    def findPosition(self, nums, target):
        if (nums == None or len(nums) == 0):
            return -1
        start = 0
        end = len(nums) - 1
        # 要点1: start + 1 < end .
        while (start + 1 < end):
	    # 要点2：start + (end - start) / 2, 2^32 - 1, result integer might overflow .
            mid = int(start + (end - start) / 2)
            # 要点3：=, <, > 分开讨论，mid 不 +1, 也不 -1 .
            if (nums[mid] == target):
                end = mid # first
                # start = mid # last
            elif (nums[mid] < target):
                start = mid
            else:
                end = mid
        # 要点4: 循环结束后，单独处理start和end.
        print("Out of loop: ", start, end)
        if (nums[start] == target):
            return start
        if (nums[end] == target):
            return end
        return -1

test = Solution()
test.findPosition(nums = [1, 2, 2, 2, 4, 5, 5], target = 2)


class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return None 
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        if nums[0] > nums[1]:
            return nums[0]
        if nums[end] > nums[end - 1]:
            return nums[end]
        while start + 1 < end:
            mid = int(start + (end - start)/2)
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return nums[mid]
            if nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                start = mid
            if nums[mid] < nums[mid - 1] and nums[mid] > nums[mid + 1]:
                end = mid
        return None

test = Solution()
test.mountainSequence(nums = [10, 9, 8, 7])
test.mountainSequence(nums = [1, 2, 4, 8, 6, 3])

### kClosestNumbers

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
        left = 1
        right = 1
        if k == 0:
            return new_arr
        while start + 1 < end:
            mid = int(start + (end - start)/2)
            if A[mid] == target:
                end = mid
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if abs(A[start] - target) <= abs(A[end] - target):
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
            elif (right + target_pos) > (len(A) - 1):
                new_arr.append(A[target_pos - left])
                left += 1
            elif abs(A[target_pos - left] - target) <= abs(A[target_pos + right] - target):
                new_arr.append(A[target_pos - left])
                left += 1
            else:
                new_arr.append(A[target_pos + right])
                right += 1
        return new_arr

test = Solution()
test.kClosestNumbers(A = [1, 4, 6, 8], target = 3, k = 3)

Chapter 3. 双指针 算法.

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        sort_nums = sorted(numbers)
        left = 0
        right = len(sort_nums) - 1 
        while (left < right):
            if sort_nums[left] + sort_nums[right] == target:
                value1 = sort_nums[left]
                value2 = sort_nums[right]
                break
            elif sort_nums[left] + sort_nums[right] < target:
                left += 1 
            else:
                right -= 1 
        print(value1, value2)
        pos1 = numbers.index(value1)
        if value1 == value2:
            pos2 = numbers.index(value2, pos1 + 1)
        else:
            pos2 = numbers.index(value2)
        if pos1 < pos2:
            return [pos1, pos2]
        else:
            return [pos2, pos1]

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        num_set = set()
        num_len = len(numbers)
        for i in range(num_len):
            if target - numbers[i] in num_set:
                pos2 = i
                value1 = target - numbers[i]
                break
            else:
                num_set.add(numbers[i])
        pos1 = numbers.index(value1)
        return [pos1, pos2]

test = Solution()
test.twoSum([2,7,11,15], 9)
test.twoSum([0, -1, 0], 0)

# https://www.lintcode.com/problem/window-sum/description

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        if nums is None or len(nums) == 0:
            return []
        start = 0
        end = len(nums)
        left = start
        right = min(k, end) - 1
        sum = 0
        for i in range(right + 1):
            sum += nums[i]
        sums = [sum]
        while right < end - 1:
            left += 1
            right += 1
            sum = sum - nums[left - 1] + nums[right]
            sums.append(sum)
        return sums

test = Solution()
test.winSum([1,2,7,8,5], 3)

# quick sort, merge sort, heap sort. O(nlogn) algorithm.


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
        temp = [None] * len(A)
        self.merge_sort(A, start, end, temp)
        print(A)
    def merge_sort(self, A, start, end, temp):
        if start >= end:
            return
        mid = int((start + end)/2)
        self.merge_sort(A, start, mid, temp)
        self.merge_sort(A, mid + 1, end, temp)
        self.merge(A, start, mid, end, temp)
    def merge(self, A, start, mid, end, temp):
        left_index = start 
        right_index = mid + 1
        temp_index = start
        print(start, mid, end)
        while (left_index <= mid and right_index <= end):
            if A[left_index] < A[right_index]:
                temp[temp_index] = A[left_index]
                left_index += 1
                temp_index += 1
            else:
                temp[temp_index] = A[right_index]
                right_index += 1
                temp_index += 1
        while left_index <= mid:
            print(temp_index, left_index, A, temp)
            temp[temp_index] = A[left_index]
            left_index += 1
            temp_index += 1
        while right_index <= end:
            temp[temp_index] = A[right_index]
            right_index += 1
            temp_index += 1
        for i in range(start, end + 1):
            A[i] = temp[i]

test = Solution()
test.sortIntegers2([1,2,7,8,5])

class Solution:
    """
    Merge Sort 2, better naming,
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return
        start = 0
        end = len(A) - 1
        sort_list = [None] * (end + 1)
        self.merge_sort(A, start, end, sort_list)
        print(A)
    def merge_sort(self, A, start, end, sort_list):
        if start >= end:
            return
        mid = int((start + end)/2)
        self.merge_sort(A, start, mid, sort_list)
        self.merge_sort(A, mid + 1, end, sort_list)
        self.merge_list(A, start, mid, end, sort_list)
    def merge_list(self, A, start, mid, end, sort_list):
        pre_index = start
        post_index = mid + 1
        sort_index = start
        while pre_index <= mid and post_index <= end:
            if A[pre_index] < A[post_index]:
                sort_list[sort_index] = A[pre_index]
                pre_index += 1
                sort_index += 1
            else:
                sort_list[sort_index] = A[post_index]
                post_index += 1
                sort_index += 1
        while pre_index <= mid:
            sort_list[sort_index] = A[pre_index]
            pre_index += 1
            sort_index += 1
        while post_index <= end:
            sort_list[sort_index] = A[post_index]
            post_index += 1
            sort_index += 1
        for i in range(start, end + 1):
            A[i] = sort_list[i]

test = Solution()
test.sortIntegers2([3,9,4,1,2,7,8,5])

class Solution:
    """
    Quick Sort, 10
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        if A is None or len(A) == 0: # handle exception,
            return
        start = 0
        end = len(A) - 1 # end, inclusive
        self.quick_sort(A, start, end)
        print(A)
    def quick_sort(self, A, start, end):
        if start >= end: # end condition of recursion,
            return
        left = start
        right = end
        mid = int((start + end)/2)
        pivot = A[mid] # Pivot value, not index 
        while (left <= right): # left <= right
            while left <= right and A[left] < pivot: # < pivot
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right: # left <= right
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        self.quick_sort(A, start, right) # recurse half
        self.quick_sort(A, left, end)

test = Solution()
test.sortIntegers2([1,4,2,7,8,5,3])
