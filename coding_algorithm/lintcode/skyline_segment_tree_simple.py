"""
a segment tree with lazy propagation

When you query a node in the segment tree, you need to make sure that all its ancestors, 
and the node itself, is properly updated. You do this while visiting the query node(s).

While visiting a query node, you traverse the path from the root to the query node, 
while taking care of all the pending updates. Since there are O(log N) ancestors you need to visit, 
for any given query node, the you do only O(log N) work.

so, https://stackoverflow.com/a/11414770/5827450 

"""
class SegmentTreeNode:
    def __init__(self,start,end):
        self.start, self.end = start, end
        self.left, self.right = None, None 
        self.max = 0

class Solution:
    def __init__(self,):
        self.lazy = {}

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
            self.lazy[root] = max(self.lazy.get(root, 0), y)
            return
        root.max = max(y, root.max)
        mid = (root.start + root.end) // 2
        if start_u <= mid:
            self.update(root.left, start_u, end_u, y)
        if end_u >= mid + 1:
            self.update(root.right, start_u, end_u, y)

    def query(self, root, start_u, end_u):
        # print(start_u, end_u, root.start, root.end, self.lazy.get(root,0))
        if start_u <= root.start and root.end <= end_u:
            return max(root.max, self.lazy.get(root, 0))
        
        root.max = max(root.max, self.lazy.get(root, 0))
        self.lazy[root.left] = max(self.lazy.get(root.left,0), self.lazy.get(root, 0))
        self.lazy[root.right] = max(self.lazy.get(root.right,0), self.lazy.get(root, 0))
        self.lazy[root] = 0
        mid = (root.start + root.end) // 2
        ans = 0
        if start_u <= mid:
            ans = self.query(root.left, start_u, end_u)
        if end_u >= mid + 1:
            ans = max(ans, self.query(root.right, start_u, end_u))
        return ans

    def buildingOutline(self, buildings):
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
        # print(xs)
        for i, x in enumerate(xs):
            x_idx[x] = i
        self.root = self.build(0, len(xs) - 1)
        sky = []
        for (start, end, y) in buildings:
            self.update(self.root, x_idx[start], x_idx[end] - 1, y)
        # print(self.lazy)
        pre_y = self.query(self.root, 0, 0)
        pre_x = xs[0]
        for x in xs:
            y = self.query(self.root, x_idx[x], x_idx[x])
            # print(x, y)
            if y != pre_y:
                if pre_y > 0:
                    sky.append((pre_x, x, pre_y))
                pre_x = x
            pre_y = y 
        # print(sky)

        return sky 


test = Solution()
buildings = [[1,3,3],[2,4,4],[5,6,1]]
r = test.buildingOutline(buildings)
print(r)

buildings = [[4,67,187],[3,80,65],[49,77,117],[67,74,9],[6,42,92],[48,67,69],
[10,13,58],[47,99,152],[66,99,53],[66,71,34],[27,63,2],[35,81,116],[47,49,10],
[68,97,175],[20,33,53],[24,94,20],[74,77,155],[39,98,144],[52,89,84],[13,65,222],
[24,41,75],[16,24,142],[40,95,4],[6,56,188],[1,38,219],[19,79,149],[50,61,174],
[4,25,14],[4,46,225],[12,32,215],[57,76,47],[11,30,179],[88,99,99],[2,19,228],
[16,57,114],[31,69,58],[12,61,198],[70,88,131],[7,37,42],[5,48,211],[2,64,106],[49,73,204],
[76,88,26],[58,61,215],[39,51,125],[13,38,48],[74,99,145],[4,12,8],[12,33,161],[61,95,190],
[16,19,196],[3,84,8],[5,36,118],[82,87,40],[8,44,212],[15,70,222],[16,25,176],[9,100,74],
[38,78,99],[23,77,43],[45,89,229],[7,84,163],[48,72,1],[31,88,123],[35,62,190],[21,29,41],
[37,97,81],[7,49,78],[83,84,132],[33,61,27],[18,45,1],[52,64,4],[58,98,57],[14,22,1],[9,85,200],
[50,76,147],[54,70,201],[5,55,97],[9,42,125],[31,88,146]]
r = test.buildingOutline(buildings)
print(r)
