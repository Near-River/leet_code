#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:
2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]
4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should
be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
"""


# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        def toplogical_sort(g, penetration, ret):
            penetration[g.label] -= 1
            ret.append(g.label)
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
        return ret if len(ret) == numCourses else []


if __name__ == '__main__':
    solution = Solution()
    print(solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
