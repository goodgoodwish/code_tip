4. BFS & Topological Sort

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

from collections import deque 
class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        if node is None:
            return
        # 1, BFS to get all nodes
        old_graph = self.get_nodes(node)
        # 2, create new nodes, store old node to new node mapping
        map_dict = {}
        for old_node in old_graph:
            map_dict[old_node] = UndirectedGraphNode(old_node.label)
        # 3, copy edges/neighbors
        for old_node in old_graph:
            for neighbor in old_node.neighbors:
                # map_dict[old_node] is new_node,
                # map_dict[neighbor] is new_neighbor,
                map_dict[old_node].neighbors.append(map_dict[neighbor])
        return map_dict[node]

    def get_nodes(self, node):
        graph = set([node])
        q = deque([node])
        while q:
            node = q.pop()
            for item in node.neighbors:
                if item not in graph:
                    graph.add(item)
                    q.append(item)
        return graph

test = Solution()
r = test.cloneGraph()
print(r)

import collections
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # Topo sort
        if prerequisites is None or len(prerequisites) <= 1:
            return True
        # get in degree
        ins = {i:0 for i in range(numCourses)}  #{1: count}
        deps = {i:[] for i in range(numCourses)} #{1: [dependent,]}
        for p in prerequisites:
            ins[p[0]] += 1
            deps[p[1]].append(p[0])  # {2:[1,3]}
        #
        q = collections.deque([k for (k,v) in ins.items() if v == 0])
        while q:
            for _ in range(len(q)):
                item = q.popleft()
                if ins[item] == 0:
                    del(ins[item])
                for dep in deps[item]:
                    ins[dep] -= 1
                    if ins[dep] == 0:
                        q.append(dep)
            # q.extend([k for (k,v) in ins.items() if v == 0 ]) # slow, time out,
        return len(ins) == 0

test = Solution()
r = test.canFinish(2, [[1,0]])
print(r)

import collections
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # init in_degree and dependency
        ins = [0 for _ in range(numCourses)] # [2,0,4]
        deps = {i:[] for i in range(numCourses)} # {2:[1,4]}
        result = []
        for pair in prerequisites:
            ins[pair[0]] += 1
            deps[pair[1]].append(pair[0])
        # BFS
        q = collections.deque([i for (i,v) in enumerate(ins) if v == 0])
        print(q)
        while q:
            next = q.popleft()
            result.append(next)
            print(result)
            for dep in deps[next]:
                ins[dep] -= 1
                if ins[dep] == 0:
                    q.append(dep)
        if len(result) == numCourses:
            return result
        else:
            return []

test = Solution()
r = test.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
print(r)

class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

import collections
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.

# {0,1,2,3,4#1,3,4#2,1,4#3,4#4}
# 1,2,3,4 are 0s neighbors, direction: from 0 to 1,2,3,4
    """
    def topSort(self, graph):
        # init graph
        in_degree = {g:0 for g in graph}
        for g in graph:
            for n in g.neighbors:
                in_degree[n] += 1
        result = []
        # BFS
        q = collections.deque([k for k,v in in_degree.items() if v == 0])
        while q:
            node = q.popleft()
            result.append(node)
            for n in node.neighbors:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    q.append(n)
        return result


import collections
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # build graph
        successor = {}
        indegree = {}
        order = []
        for seq in seqs:
            if len(seq) == 0:
                continue
            if seq[0] not in indegree:
                indegree[seq[0]] = 0
            for i in range(len(seq) - 1):
                if seq[i + 1] not in indegree:
                    indegree[seq[i + 1]] = 1
                else:
                    indegree[seq[i + 1]] += 1
                if seq[i] not in successor:
                    successor[seq[i]] = [seq[i + 1]]
                else:
                    successor[seq[i]].append(seq[i + 1])
        #BFS
        q = collections.deque([k for (k,v) in indegree.items() if v == 0])
        while q:
            if len(q) != 1:
                return False 
            next = q.popleft()
            order.append(next)
            print(next)
            if next not in successor:
                continue
            for node in successor[next]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)
        if order == org:
            return True 
        return False 

org = [1,2,3]; seqs = [[1,2],[1,3],[2,3]]
test = Solution()
r = test.sequenceReconstruction(org, seqs)
print(r)
org = [4,1,5,2,6,3]
seqs = [[5,2,6,3],[4,1,5,2]]
r = test.sequenceReconstruction(org, seqs)
print(r)
org = [1]
seqs = [[],[]]
r = test.sequenceReconstruction(org, seqs)
print(r)

from collections import deque 
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if grid is None or len(grid) == 0:
            return 0
        # init, Depth, Width
        d = len(grid)
        w = len(grid[0])
        count = 0
        # find a 1,
        for x in range(d):
            for y in range(w):
                if grid[x][y] == 1:
                    count += 1
                    self.bfs(grid, x, y)
        return count
    def bfs(self, grid, x, y):
        q = deque([(x, y)])
        steps = [[0,1],[1,0],[-1,0],[0,-1]]
        while q:
            (x,y) = q.popleft()
            grid[x][y] = 0
            # find neighbor
            for step in steps:
                x1, y1 = x + step[0], y + step[1]
                if not self.is_valid(grid, x1, y1):
                    continue
                q.append((x1, y1))
                grid[x1][y1] = 0
    def is_valid(self, grid, x, y):
        d = len(grid)
        w = len(grid[0])
        if 0 <= x < d and 0 <= y < w and grid[x][y] == 1:
            return True 
        return False

grid = [
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]

test = Solution()
r = test.numIslands(grid)
print(r)

grid = [[]]
grid = [[0]]

if grid:
    print("True")

if grid[0]:
    print("True")

if grid[0][0]:
    print("True")

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

from collections import deque 
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        if not grid or not grid[0]:
            return -1
        # BFS
        # mark visited
        # find, return count, or -1
        changes = [
            [+1, +2],
            [+1, -2],
            [-1, +2],
            [-1, -2],
            [+2, +1],
            [+2, -1],
            [-2, +1],
            [-2, -1]
        ]
        count = 0
        q = deque([source])
        while q:
            count += 1
            q_size = len(q)
            print("q size:", q_size)
            print("grid:", grid)
            for _ in range(q_size):
                pos = q.popleft()
                for chg in changes:
                    new_point = Point(pos.x + chg[0], pos.y + chg[1])
                    if new_point.x == destination.x and new_point.y == destination.y:
                        return count
                    if self.is_valid(new_point, grid):
                        q.append(new_point)
                        grid[new_point.x][new_point.y] = True
        return -1
    def is_valid(self, point, grid):
        depth = len(grid)
        width = len(grid[0])
        if 0 <= point.x < depth and 0 <= point.y < width and grid[point.x][point.y] is not True:
            return True
        return False

grid = [[False,False,False],[False,False,False],[False,False,False]]
source = Point(2,0)
destination = Point(2,2)
test = Solution()
r = test.shortestPath(grid, source, destination)
print(r)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

from collections import deque 
class Solution:
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
        root = TreeNode(int(s[0]))
        start = 1
        q = deque([root])
        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                left_val = s[start + i*2]
                if left_val != "#":
                    node.left = TreeNode(int(left_val))
                    q.append(node.left)
                right_val = s[start + i*2 + 1]
                if right_val != "#":
                    node.right = TreeNode(int(right_val))
                    q.append(node.right)
            start += level_size * 2
        return root

node = TreeNode(3)
node.left = TreeNode(2)
node.left.left = TreeNode(1)
test = Solution()
r = test.serialize(node)
print(r)
r = test.deserialize(r)
print(r.val)


from collections import deque 
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        count = 1
        size = len(start)
        abc = "abcdefghijklmnopqrstuvwxyz"
        q = deque([start])
        visited = set()
        while q:
            print(count, q)
            count += 1
            for _ in range(len(q)):
                word = q.popleft()
                visited.add(word)
                for i in range(size):
                    for letter in abc:
                        next = word[:i] + letter + word[i+1:]
                        if next == end:
                            return count 
                        if next not in visited and next in dict:
                            q.append(next)
                            visited.add(next)
        return 0



start = "a"
end = "a"
dict = ["b"]
test = Solution()
r = test.ladderLength(start, end, dict)
print(r)

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
r = test.ladderLength(start, end, dict)
print(r)

abc = ""
for i in range(26):
    abc += chr(ord("a") + i)
print(abc)
