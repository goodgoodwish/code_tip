class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from collections import deque 
class Construct:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        if root is None:
            return
        s = [str(root.val)]
        q = deque([root])
        while q:
            q_size = len(q)
            for _ in range(q_size):
                node = q.popleft()
                if node.left:
                    s.append(str(node.left.val))
                    q.append(node.left)
                else:
                    s.append("#")
                if node.right:
                    s.append(str(node.right.val))
                    q.append(node.right)
                else:
                    s.append("#")
        result = ",".join(s)
        return result

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        if data is None or len(data) == 0:
            return
        s = data.split(",")
        s_size = len(s)
        root = TreeNode(int(s[0]))
        start = 1
        q = deque([root])
        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                # print("index:", start + i*2, s[start + i*2])
                left_val = s[start + i*2]
                if left_val != "#":
                    node.left = TreeNode(int(left_val))
                    q.append(node.left)
                right_val = s[start + i*2 + 1]
                if right_val != "#":
                    node.right = TreeNode(int(right_val))
                    q.append(node.right)
            start += level_size * 2
            if start >= s_size:
                break
        return root

test = Construct()
r = test.deserialize("4,3,7,#,#,5,6")
print(r.val)



class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here


test = Solution()
r = test.isValidBST(r)
print("is BST", r)


  4
 / \
3   7
   / \
  5   6

LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7