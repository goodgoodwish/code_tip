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

