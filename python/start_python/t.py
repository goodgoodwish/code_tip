class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        # write your code here
        pass

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
# r = test.permutationIndex([1,2,4])
r = test.permute([2,2,2,4])
print(r)
