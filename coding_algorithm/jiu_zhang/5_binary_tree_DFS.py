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
