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

Chapter 3

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
