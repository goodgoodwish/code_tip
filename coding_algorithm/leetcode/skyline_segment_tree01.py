# It was accepted in Leetcode, but Time Limit Exceeded in Lintcode.
#
# Runtime: 416 ms, faster than 7.21% of Python3 online submissions for The Skyline Problem.

class SegmentTreeNode:
    def __init__(self,start,end):
        self.start, self.end = start, end
        self.left, self.right = None, None 
        self.max = 0

class Solution:

    def build(self, start, end):
        root = SegmentTreeNode(start, end)
        if start == end:
            return root
        mid = (start + end)//2
        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)
        # root.max = (root.left.max, root.left.max)
        return root

    def update(self, root, start_u, end_u, y):
        if end_u < root.start or root.end < start_u:
            print("range ", start_u, end_u, " out of range.")
            return
        if start_u <= root.start and root.end <= end_u:
            root.max = max(y, root.max)
            return
        mid = (root.start + root.end) // 2
        if start_u <= mid:
            self.update(root.left, start_u, end_u, y)
        if end_u >= mid + 1:
            self.update(root.right, start_u, end_u, y)

    def query_index(self, root, index):
        if root.start == index == root.end:
            return root.max
        
        mid = (root.start + root.end) // 2
        ans = 0
        if index <= mid:
            ans = self.query_index(root.left, index)
        if index >= mid + 1:
            ans = self.query_index(root.right, index)
        ans = max(root.max, ans)
        return ans

    def getSkyline(self, buildings):
        results = []
        if not buildings:
            return results
        xs = []
        x_idx = {}
        for (start, end, _) in buildings:
            xs.append(start)
            xs.append(end)
        xs = list(set(xs))
        xs.sort()
        for i, x in enumerate(xs):
            x_idx[x] = i
        self.root = self.build(0, len(xs) - 1)
        sky = []
        for (start, end, y) in buildings:
            self.update(self.root, x_idx[start], x_idx[end] - 1, y)
        pre_y = 0
        for x in xs:
            y = self.query_index(self.root, x_idx[x])
            if y != pre_y:
                sky.append((x, y)) # leet code
            pre_y = y 

        return sky 