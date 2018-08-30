class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []
        path, A = [], []
        # path = [str(root.val)]
        self.traverse(root, path, A)
        return A
    def traverse(self, root, path, A):
        if root.left is None and root.right is None:
            path.append(str(root.val))
            A.append("->".join(path))
            print(path)
        # path.append(str(root.val))
        if root.left:
            path.append(str(root.val))
            self.traverse(root.left, path, A)
            path.pop() 
        if root.right:
            path.append(str(root.val))
            self.traverse(root.right, path, A)
            path.pop()

#

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
#

b_tree = TreeNode(5)
b_tree.left = TreeNode(3)
b_tree.left.left = TreeNode(1)
b_tree.right = TreeNode(2)
b_tree.right.left = TreeNode(-7)
b_tree.right.right = TreeNode(-10)

test = Solution()
l = test.binaryTreePaths(b_tree)
print("root:", l)
