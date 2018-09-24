class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of segment tree.
    @param index: index.
    @param value: value
    @return: nothing
    """
    def build(self, A):
        start = 0
        end = len(A) - 1
        root = self.build_st(A, start, end)
        return root
    def build_st(self, A, start, end):
        if start > end:
            return
        root = SegmentTreeNode(start, end)
        if start == end:
            root.max = A[start]
            return root
        mid = (start + end)//2
        root.left = self.build_st(A, start, mid)
        root.right = self.build_st(A, mid + 1, end)
        root.max = max(root.left.max, root.right.max)
        return root
    def modify(self, root, index, value):
        # write your code here

test = Solution()
nums = [2,1,0,3]
root = test.build(nums)

def print_st(root):
    if root is None:
        return
    print(f"{root.start}, {root.end} : {root.max}, {root.sum} ")
    print_st(root.left)
    print_st(root.right)

print_st(root)

index = 2
value = 4
r = test.modify(root, index, value)
print(r)

print_st(root)
