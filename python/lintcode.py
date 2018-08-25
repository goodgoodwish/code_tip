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

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        if colors is None or len(colors) == 1:
            return 
        end = len(colors) - 1
        self.sort_range(colors, 1, k, 0, end)
        print(colors)
    def sort_range(self, arr, k_start, k_end, arr_start, arr_end):
        if k_start == k_end:
            return
        k_mid = k_start + int((k_end - k_start)/2)
        arr_mid = self.sort_color(arr, k_mid, arr_start, arr_end)
        self.sort_range(arr, k_start, k_mid, arr_start, arr_mid)
        self.sort_range(arr, k_mid + 1, k_end, arr_mid, arr_end)
    def sort_color(self, arr, k_mid, start_index, end_index):
        if start_index >= end_index:
            return 
        left = start_index 
        right = end_index 
        while left <= right:
            while left <= right and arr[left] <= k_mid:
                left += 1
            while left <= right and arr[right] > k_mid:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return right

test = Solution()
test.sortColors2([3, 2, 2, 1, 4], 4)
test.sortColors2([3, 2, 2, 1, 4,5,6,7,6,5,4,3,2,1], 7)

test.sortColors2([2,1,1,2,2],2)

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return 
        i0, i1 = 0, 0
        i2 = len(nums) - 1
        while i1 <= i2:
            if nums[i1] == 0:
                nums[i1], nums[i0] = nums[i0], nums[i1]
                i0 += 1
                i1 += 1
            elif nums[i1] == 1:
                i1 += 1
            elif nums[i1] == 2:
                nums[i1], nums[i2] = nums[i2], nums[i1]
                i2 -= 1
            print(nums, i0, i1, i2)
        print(nums)

test = Solution()
test.sortColors([2, 1, 0, 0, 1, 2])
test.sortColors([1, 2, 2, 1, 0])
test.sortColors([2,0,0,1,2,0,2])

https://www.lintcode.com/problem/search-in-rotated-sorted-array/

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
            elif A[mid] <= right_high and target > right_high:
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
test.search([4, 5, 1, 2, 3], 4)
test.search([4, 5, 6, 7, 1, 2, 3], 9)
test.search([4, 5, 6, 7, 1], 1)
test.search([1, 2, 3], 1)

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        right_high = nums[end]
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] > right_high:
                start = mid
            else:
                end = mid
        return min(nums[start], nums[end] )

test = Solution()
test.findMin([4, 5, 1, 2, 3])

class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n < 0:
            n = -n 
            x = 1/x 
        if n == 0:
            return 1
        if n > 1000:
            n = 1000
        n_half = n // 2
        if n % 2 == 1:
            return x * self.myPow(x, n_half) * self.myPow(x, n_half)
        else:
            return self.myPow(x, n_half) * self.myPow(x, n_half)

test = Solution()
test.myPow(2, 2)
test.myPow(2, 3)
test.myPow(34.00515, -3)
test.myPow(2.0, -2147483648)
test.myPow(2.0, -2047483648)


class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    def pow(self, x, n):
        # write your code here
        if n < 0:
            x = 1/x
            n = -n
        result = 1
        base = x
        while n > 0:
            if n%2 == 1:
                result = base * result
            base *= base
            n = n // 2 
        return result

test = Solution()
test.pow(2, 2)
test.pow(2, 3)
test.pow(34.00515, -3)
test.pow(2.0, -2147483648)


7 = 4 + 2 + 1 = 0B111 = 2^4 * 2^2 * 2^1
                        ^    <==    ^
                        |           |
move bit to right, if current right most bit is 1, result = previous_result * current_base.

7 >> 1 = 3 = 2 + 1 = 0B11
7 >> 2 = 3 >> 1 = 1 = 0B1

class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    def pow(self, x, n):
        if n < 0:
            n = -n
            x = 1/x
        if n == 0:
            return 1
        base = x
        result = 1
        while n > 0:
            if n % 2 == 1:
                result = result * base
            base *= base
            n = n >> 1
            if n > 1 and (result < 0.01 or base < 0.01):
                return 0.00
        return result

test = Solution()
test.pow(2, 3)

class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    Iterative. without recursion. Non Recursive Approach.
    .
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        node = root
        A = []
        stack = []
        while ((node is not None) or stack):
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                A.append(node.val)
                print("node pop", node.val)
                node = node.right
                right_val = (node.val if node else "-")
                print("node right", right_val)
        return A

bst = TreeNode(5)
bst.left = TreeNode(3)
bst.left.left = TreeNode(1)
bst.right = TreeNode(8)
bst.right.left = TreeNode(7)
bst.right.right = TreeNode(10)
bst.right.right.right = TreeNode(15)
test = Solution()
test.inorderTraversal(bst)

class Solution:
    """
    Recursive Approach.
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def __init__(self):
        self.A = []
    def inorderTraversal(self, root):
        # write your code here
        if root is None:
            return self.A
        self.inorderTraversal(root.left)
        self.A.append(root.val)
        self.inorderTraversal(root.right)
        return self.A

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        A = []
        def travel(root):
            if root is None:
                return
            travel(root.left)
            travel(root.right)
            A.append(root.val)
        travel(root)
        return A

bst = TreeNode(5)
bst.left = TreeNode(3)
bst.left.left = TreeNode(1)
bst.right = TreeNode(8)
bst.right.left = TreeNode(7)
test = Solution()
test.postorderTraversal(bst)

class Solution:
    """
    iterative postorder binary tree traversal, without recursion.
    
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        if root == None:
            return []
        last_visit_node = None 
        node = root
        stack = []
        A = []
        while node != None or stack:
            if node != None: 
                stack.append(node)
                node = node.left
            else:
                peek_node = stack[-1]
                print("peek node", peek_node.val)
                # end of left child, or move up on left child,
                # if right child exists, traversing right child node,
                # from left child, then move to right child
                if peek_node.right != None and last_visit_node != peek_node.right:
                    node = peek_node.right 
                else:
                    last_visit_node = stack.pop()
                    A.append(last_visit_node.val)
                    # A.append(peek_node.val)
                    # last_visit_node = stack.pop()
        print(A)
        return A

bst = TreeNode(5)
bst.left = TreeNode(3)
bst.left.left = TreeNode(1)
bst.right = TreeNode(8)
bst.right.left = TreeNode(7)
test = Solution()
test.postorderTraversal(bst)
