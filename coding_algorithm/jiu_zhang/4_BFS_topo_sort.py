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
