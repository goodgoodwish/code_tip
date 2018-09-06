class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        if root is None:
            return []
        stack_upper, stack_lower, A = [], [], []
        self.find_target(root, target, stack_upper)
        stack_lower = stack_upper[:]
        if stack_upper[-1].val < target:
            self.move_upper(stack_upper)
        else:
            self.move_lower(stack_lower)
        for _ in range(k):
            if not stack_upper:
                A.append(stack_lower[-1].val)
                self.move_lower(stack_lower)
            elif not stack_lower:
                A.append(stack_upper[-1].val)
                self.move_upper(stack_upper)
            elif stack_upper[-1].val - target < target - stack_lower[-1].val:
                A.append(stack_upper[-1].val)
                self.move_upper(stack_upper)
            else:
                A.append(stack_lower[-1].val)
                self.move_lower(stack_lower)
        return A
    def find_target(self, root, target, stack):
        while root:
            stack.append(root)
            if target < root.val:
                root = root.left
            else:
                root = root.right
    def move_upper(self, stack):
        curr = stack[-1]
        if curr.right:
            node = curr.right
            while node:
                stack.append(node)
                node = node.left
        else:
            visited_node = stack.pop() 
            while stack and stack[-1].right == visited_node:
                visited_node = stack.pop()
    def move_lower(self, stack):
        curr = stack[-1]
        if curr.left:
            node = curr.left
            while node:
                stack.append(node)
                node = node.right
        else:
            visited_node = stack.pop() 
            while stack and stack[-1].left == visited_node:
                visited_node = stack.pop()


#

bst = TreeNode(5)
bst.left = TreeNode(3)
bst.left.left = TreeNode(1)
bst.right = TreeNode(8)
bst.right.left = TreeNode(7)
bst.right.right = TreeNode(10)

test = Solution()
l = test.closestKValues(bst,4,6)
print(l)

bst = TreeNode(1)
test = Solution()
l = test.closestKValues(bst,0.0,1)
print(l)

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # Traversal, 
        self.min_node = None
        self.min_value = float("inf")
        def min_tree(root):
            if root is None:
                return 0
            current_sum = min_tree(root.left) + min_tree(root.right) + root.val
            if current_sum < self.min_value:
                self.min_node = root
                self.min_value = current_sum 
            return current_sum
        min_tree(root)
        return self.min_node

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # Divid and Conquer
        _, min_node, _ = self.min_tree(root)
        return min_node
    def min_tree(self, root):
        if root is None:
            return float("inf"), None, 0
        min_left, min_left_tree, sum_left = self.min_tree(root.left)
        min_right, min_right_tree, sum_right = self.min_tree(root.right)
        #
        current_sum = sum_left + sum_right + root.val
        current_min = min(min_left, min_right, current_sum)
        if min_left == current_min:
            return current_min, min_left_tree, current_sum
        if min_right == current_min:
            return current_min, min_right_tree, current_sum
        return current_min, root, current_sum

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
l = test.findSubtree(b_tree)
print("root:", l.val)

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        if root is None:
            return []
        A = []
        path = [str(root.val)]
        self.traverse(root, path, A)
        return A
    def traverse(self, root, path, A):
        if root.left is None and root.right is None:
            A.append("->".join(path))
            print(path)
        # path.append(str(root.val))
        if root.left:
            path.append(str(root.left.val))
            self.traverse(root.left, path, A)
            path.pop() 
        if root.right:
            path.append(str(root.right.val))
            self.traverse(root.right, path, A)
            path.pop()

b_tree = TreeNode(5)
b_tree.left = TreeNode(3)
b_tree.right = TreeNode(2)

test = Solution()
l = test.binaryTreePaths(b_tree)
print("root:", l)

class Solution:
    def binaryTreePaths(self, root):
        # Divider Conquer with DFS
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        paths = []
        for path in self.binaryTreePaths(root.left):
            paths.append(str(root.val) + "->" + path)
        for path in self.binaryTreePaths(root.right):
            paths.append(str(root.val) + "->" + path)
        return paths

class Solution:
    def closestValue(self, root, target):
        # write your code here
        min_diff = float("inf")
        while root:
            if abs(root.val - target) < min_diff:
                value = root.val
                min_diff = abs(root.val - target)
            if target > root.val:
                root = root.right
            else:
                root = root.left
            if root:
                prev_value = value
        return value

