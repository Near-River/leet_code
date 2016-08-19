#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:
2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should
also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.

Hints:
    1. This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological ordering
    exists and therefore it will be impossible to take all courses.
    2. Topological Sort via DFS.
    3. Topological sort could also be done via BFS.
"""


# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # Tags: Graph & TopLogical Sort
        def toplogical_sort(g, penetration, ret):
            penetration[g.label] -= 1
            ret.append(g)
            for neighbor in g.neighbors:
                penetration[neighbor.label] -= 1
                if penetration[neighbor.label] == 0:
                    toplogical_sort(neighbor, penetration, ret)

        graph = []
        penetration = [0] * numCourses
        for i in range(numCourses):
            graph.append(DirectedGraphNode(i))
        for p in prerequisites:
            (graph[p[1]]).neighbors.append(graph[p[0]])
            penetration[p[0]] += 1
        ret = []
        for g in graph:
            if penetration[g.label] == 0:
                toplogical_sort(g, penetration, ret)
        return len(ret) == numCourses


if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(2, [[1, 0]]))
    print(solution.canFinish(2, [[1, 0], [0, 1]]))
