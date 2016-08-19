#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TopLogical Sorting: Depth-first-search
"""


# Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def dfs(self, i, countrd, ans):
        ans.append(i)
        countrd[i] -= 1
        for j in i.neighbors:
            countrd[j] -= 1
            if countrd[j] == 0:
                self.dfs(j, countrd, ans)

    def topSort(self, graph):
        """
        :param graph: A list of Directed graph node
        :return: A list of integer
        """
        countrd = {}
        for x in graph:
            countrd[x] = 0
        for i in graph:
            for j in i.neighbors:
                countrd[j] += 1

        ans = []
        for i in graph:
            if countrd[i] == 0:
                self.dfs(i, countrd, ans)
        return ans


if __name__ == '__main__':
    pass
