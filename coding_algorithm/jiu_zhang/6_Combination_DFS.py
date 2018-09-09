# 6. Combination-based DFS

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        if nums is None:
            return
        result = []
        nums.sort()
        self.dfs(nums, 0, [], result)
        return result
    # backtracking
    def dfs(self, nums, start, subset, result):
        result.append(subset[:]) # deep copy
        size = len(nums)
        print(start)
        for i in range(start, size):
            subset.append(nums[i])
            print(subset)
            self.dfs(nums, i + 1, subset, result)
            subset.pop()

test = Solution()
r = test.subsets([1,2,3])
print(r)

for i in range(4,3):
    print(i)  # print nothing, 4 > 3, exit.

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        if len(s) == 0:
            return []
        def dfs(s, wordDict, memo):
            if len(s) == 0:
                return [""]
            if s in memo:
                return memo[s]
            lines = []
            for i in range(1, len(s) + 1):
                prefix = s[:i]
                if prefix in wordDict:
                    # print(prefix)
                    sublines = dfs(s[i:], wordDict, memo)
                    for subline in sublines:
                        # print(subline)
                        subline = " " + subline if subline else ""
                        lines.append(prefix + subline)
                        # print("lines:", lines)
            memo[s] = lines
            return lines
        memo = {}
        results = dfs(s, wordDict, memo)
        return results

class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        def dfs(s, wordDict, memo):
            s_len = len(s)
            if s_len == 0:
                return
            if s in memo:
                return memo[s]
            lines = []
            if s in wordDict:
                lines.append(s)
            for i in range(1, s_len):
                prefix = s[:i]
                if prefix in wordDict:
                    sublines = dfs(s[i:], wordDict, memo)
                    for subline in sublines:
                        lines.append(prefix + " " + subline)
            memo[s] = lines
            return lines
        memo = {}
        results = dfs(s, wordDict, memo)
        return results

test = Solution()
s = "lintcode"
wordDict = set(["de", "ding", "co", "code", "lint", "lintcode"])
r = test.wordBreak(s, wordDict)
print(r)

# https://www.lintcode.com/problem/wildcard-matching

class Solution:
    """
    no Memoization version
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        def dfs(s,i,p,j):
            if i == len(s):
                if p[j:] == "*" * (len(p) - j):
                    return True
                return False 
            if j == len(p):
                return False 
            if p[j] != "*":
                matched = is_char_match(s[i], p[j]) and dfs(s,i + 1, p, j + 1)
            if p[j] == "*":
                matched = dfs(s, i, p, j + 1) or dfs(s, i + 1, p, j)
            return matched
        def is_char_match(s_char, p_char):
            return s_char == p_char or p_char == "?"
        matched = dfs(s, 0, p, 0)
        return matched


test = Solution()
s = "aac"
p = "a*"
r = test.isMatch(s, p)
print(r)
r = test.isMatch("", "")
print(r)

class Solution:
    """
    Memoization version
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        def dfs(s, i, p, j, memo):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(s):
                if p[j:] == "*" * (len(p) - j):
                    memo[(i,j)] = True
                    return memo[(i,j)]
                memo[(i,j)] = False
                return memo[(i,j)] 
            if j == len(p): # and i > len(s)
                memo[(i,j)] = False
                return memo[(i,j)] 
            if p[j] != "*":
                matched = is_char_match(s[i], p[j]) and dfs(s,i + 1, p, j + 1, memo)
            if p[j] == "*":
                matched = dfs(s, i, p, j + 1, memo) or dfs(s, i + 1, p, j, memo)
            memo[(i,j)] = matched
            return memo[(i,j)]
        def is_char_match(s_char, p_char):
            return s_char == p_char or p_char == "?"
        memo = {}
        matched = dfs(s, 0, p, 0, memo)
        return matched


test = Solution()
s = "aac"
p = "a*"
r = test.isMatch(s, p)
print(r)
r = test.isMatch("", "")
print(r)

# https://www.lintcode.com/problem/regular-expression-matching

class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        def dfs(s, i, p, j, memo):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(s):
                if j == len(p) or p[j+1:] == "*" * (len(p) - j - 1):
                    memo[(i,j)] = True
                    return memo[(i,j)]
                memo[(i,j)] = False
                return memo[(i,j)] 
            if j == len(p): # and i > len(s)
                memo[(i,j)] = False
                return memo[(i,j)] 
            if j + 1 < len(p) and p[j + 1] == "*":
                matched = dfs(s, i, p, j + 2, memo) or (dfs(s, i + 1, p, j, memo) and is_char_match(s[i], p[j]))
            else:
                matched = is_char_match(s[i], p[j]) and dfs(s,i + 1, p, j + 1, memo)
            memo[(i,j)] = matched
            return memo[(i,j)]
        def is_char_match(s_char, p_char):
            return s_char == p_char or p_char == "."
        memo = {}
        matched = dfs(s, 0, p, 0, memo)
        return matched

test = Solution()
r = test.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
print(r)
s = "aac"
p = "a*c"
r = test.isMatch(s, p)
print(r)
r = test.isMatch("", "")
print(r)
