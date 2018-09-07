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
