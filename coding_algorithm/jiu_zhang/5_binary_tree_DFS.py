# 5. Binary Tree DFS 

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

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        def inorder(root):
            if root is None:
                return None, None
            if root.left is None and root.right is None:
                head = root
                tail = root
                return (head, tail)
            next_right = root.right if root.right else None
            if root.left:
                (head, tail) = inorder(root.left)
                root.right = head
                tail.right = next_right
                root.left = None
            if next_right:
                (_, tail) = inorder(root.right)
            head = root
            return(head, tail)
        head, tail = inorder(root)
        return head

#    2
# 3     4

# 2 -> 3 -> 4

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        def postorder(root):
            if root is None:
                return True, 0
            if root.left is None and root.right is None:
                return True, 1
            left_h = 0
            right_h = 0
            left_bal, right_bal = True, True
            if root.left:
                left_bal, left_h = postorder(root.left)
            if root.right:
                right_bal, right_h = postorder(root.right)
            if not (right_bal and left_bal):
                return False, 0
            if abs(left_h - right_h) > 1:
                return False, 0
            else:
                return True, max(left_h, right_h) + 1
        bal, h = postorder(root)
        return bal 

b_tree = TreeNode(5)
b_tree.left = TreeNode(3)
b_tree.right = TreeNode(2)
b_tree.right.right = TreeNode(1)

test = Solution()
r = test.isBalanced(b_tree)
print("root:", r)

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        def check_tree(root):
            # Divide and conquer,
            if root is None:
                return True, None, None
            if root.left is None and root.right is None:
                return True, root.val, root.val
            left_is_bst, right_is_bst = True, True
            left_max, left_min = -float("inf"), float("inf")
            right_max, right_min = -float("inf"), float("inf")
            if root.left:
                left_is_bst, left_max, left_min = check_tree(root.left)
            if root.right:
                right_is_bst, right_max, right_min = check_tree(root.right)
            curr_min = min(root.val, left_min, right_min)
            curr_max = max(root.val, left_max, right_max)
            if not (left_is_bst and right_is_bst):
                return False, 0, 0
            if left_max < root.val < right_min:
                return True, curr_max, curr_min
            return False, 0, 0
        result, _, _ = check_tree(root)
        return result

# r = test.deserialize("2,1,4,#,#,3,5")
test = Solution()
r = test.isValidBST(r)
print("is BST", r)

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def __init__(self):
        self.is_valid = True
        self.last_value = -float("inf")
    def inorder(self, root):
        # inorder traverse, should be in ascending,
        if self.is_valid is False:
            return
        if root is None:
            return
        if root.left:
            self.inorder(root.left)
        # Visit node in middle,
        if root.val <= self.last_value:
            self.is_valid = False
            return
        self.last_value = root.val
        if root.right:
            self.inorder(root.right)
    def isValidBST(self, root):
        self.inorder(root)
        return self.is_valid

    def lowestCommonAncestor3(self, root, A, B):
        a, b = A.val, B.val
        def search_ab(root,a,b):
            if not root:
                return None, None 
            r1,r2,n1,n2 = None,None,None,None 
            if a == b and root.val == a:
                return 0, root
            if root.left is None and root.right is None:
                return root.val, None
            if root.left:
                r1, n1 = search_ab(root.left, a, b)
            if root.right:
                r2, n2 = search_ab(root.right, a, b)
            if n1 or n2:
                return 0, n1 or n2
            # print("val,a,b,r1,r2", root.val, a, b, r1, r2)
            if r1 in (a, b) and r2 in (a, b):
                print(root.val, a, b)
                return 0, root
            if (root.val in (a, b) and (r1 in (a, b) or r2 in (a, b))):
                print(root.val, a, b)
                return 0, root
            if r1 in (a, b):
                return r1, None
            if r2 in (a,b):
                return r2, None
            return root.val, None
        _, Node = search_ab(root, a, b)
        return Node

tree = Construct()
root = tree.deserialize("4,3,7,#,#,5,6")
print(root.val)

r = test.lowestCommonAncestor3(root, A, B)
print("LCA is", r)
