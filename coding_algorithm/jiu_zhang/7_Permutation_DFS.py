# 7. Permutation and Graph based DFS,

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def dfs(self, nums, perm, visited, results):
        nums_size = len(nums)
        if len(perm) == nums_size:
            results.append(list(perm))
            return
        for i in range(nums_size):
            if visited[i]:
                continue
            perm.append(nums[i])
            visited[i] = True
            self.dfs(nums, perm, visited, results)
            perm.pop()
            visited[i] = False

    def permute(self, nums):
        if nums is None:
            return
        perm = []
        results = []
        visited = [False for _ in range(len(nums))]
        self.dfs(nums, perm, visited, results)
        return results 

test = Solution()
r = test.permute([2,3,4])
print(r)

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        def dfs_uk(nums,perm,visited,results):
            size = len(nums)
            if len(perm) == size:
                results.append(perm[:])
            for i in range(size):
                if visited[i]:
                    continue 
                if i > 0 and nums[i - 1] == nums[i] and (not visited[i - 1]):
                    continue
                perm.append(nums[i])
                visited[i] = True
                dfs_uk(nums, perm, visited, results)
                visited[i] = False
                perm.pop()
        if nums is None:
            return 
        perm = []
        visited = [False for _ in range(len(nums))]
        results = []
        dfs_uk(nums,perm,visited,results)
        return results


test = Solution()
r = test.permute([2,2,2,4])
print(r)

class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
        def dfs(n, y, locs, results):
            if len(locs) == n:
                results.append(locs[:])
            for x in (range(n)):
                if not is_valid(x, y, locs):
                    continue 
                locs.append((x,y))
                dfs(n, y+1, locs, results)
                locs.pop()
        def is_valid(x, y, locs):
            for x1, y1 in locs:
                if x1 == x or x+y == x1+y1 or x-y==x1-y1:
                    return False
            return True 
        results = []
        dfs(n, 0, [], results)
        return len(results)


test = Solution()
r = test.totalNQueens(8)
print(r)

class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def solveNQueens(self, n):
        # write your code here
        def dfs(n, y, locs, results):
            if len(locs) == n:
                results.append(locs[:])
            for x in (range(n)):
                if not is_valid(x, y, locs):
                    continue 
                locs.append((x,y))
                dfs(n, y+1, locs, results)
                locs.pop()
        def is_valid(x, y, locs):
            for x1, y1 in locs:
                if x1 == x or x+y == x1+y1 or x-y==x1-y1:
                    return False
            return True 
        def draw_chess_board(n, grid):
            str_results = []
            for locs in grid:
                solution = []
                for loc in locs:
                    (x, y) = loc
                    row_str = "".join(["Q" if x == i else "." for i in range(n)])
                    solution.append(row_str)
                str_results.append(solution[:])
            return str_results
        results = []
        dfs(n, 0, [], results)
        ans = draw_chess_board(n, results)
        return ans


test = Solution()
r = test.solveNQueens(4)
print(r)

class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def solveNQueens(self, n):
        visited = {
            "col": set(),
            "sum": set(),
            "diff": set(),
        }
        def build_chess_board(cols):
            grid = []
            n = len(cols)
            for col in cols:
                grid.append("".join(["Q" if col == i else "." for i in range(n)]))
            return grid
        def dfs(n, cols, visited, results):
            row = len(cols)
            if row == n:
                results.append(build_chess_board(cols))
                return
            for col in range(n):
                if not is_valid(row, col, visited):
                    continue 
                visited["col"].add(col)
                visited["sum"].add(row + col)
                visited["diff"].add(row - col)
                cols.append(col)
                dfs(n, cols, visited, results)
                cols.pop()
                visited["col"].remove(col)
                visited["sum"].remove(row + col)
                visited["diff"].remove(row - col)
        def is_valid(row, col, visited):
            if (col in visited["col"] or \
              (row + col) in visited["sum"] or \
              (row - col) in visited["diff"]):
                return False
            return True
        results = []
        dfs(n, [], visited, results)
        return results

test = Solution()
r = test.solveNQueens(5)
print(r)

class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def is_match(self, p, s, word_map, used):
        if not p:
            return not s
        if p[0] in word_map:
            word = word_map[p[0]]
            if not s.startswith(word):
                return False
            return self.is_match(p[1: ],s[len(word): ], word_map, used )
        for i in range(len(s)):
            if s[ :i + 1] in used:
                continue 
            word = s[ :i + 1]
            word_map[p[0]] = word
            used.add(word)
            if self.is_match(p[1:], s[i+1: ], word_map, used):
                return True
            del word_map[p[0]]
            used.remove(word)
        return False 
    def wordPatternMatch(self, pattern, str):
        word_map = {}
        used = set()
        return self.is_match(pattern, str, word_map, used)


test = Solution()
r = test.wordPatternMatch("abab","eeddeedd")
print(r)
r = test.wordPatternMatch("abab","eeddeeddf")
print(r)

DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def dfs(self, board, words, prefix_set, word, pos, row, col, results):
        if not self.is_inside(row, col, board):
            return
        if (row, col) in pos:
            return
        word += board[row][col]
        if word not in prefix_set:
            return
        if word in words:
            results.add(word)
        for (r1, c1) in DIRECTION:
            pos.add((row, col))
            self.dfs(board, words, prefix_set, word, pos, row + r1, col + c1, results)
            pos.remove((row, col))
    def is_inside(self, row, col, board):
        depth = len(board)
        width = len(board[0])
        if 0 <= row < depth and 0 <= col < width:
            return True 
        return False
    def wordSearchII(self, board, words):
        depth = len(board)
        if not board or depth == 0:
            return []
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i+1])
        results = set()
        pos = set()
        for r in range(depth):
            for c in range(len(board[0])):
                self.dfs(board, words, prefix_set, "", pos, r, c, results)
        return list(results)

board = ["doaf","agai","dcan"]
words = ["dog","dad","dgdg","can","again"]

test = Solution()
r = test.wordSearchII(board, words)
print(r)

