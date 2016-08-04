#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Note: m and n will be at most 100.
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path = []
        for i in range(m):
            temp = []
            for j in range(n): temp.append(0)
            path.append(temp)
        path[m - 1][n - 1] = 1
        i = m - 1
        while i >= 0:
            j = n - 1
            while j >= 0:
                if i + 1 < m: path[i][j] += path[i + 1][j]
                if j + 1 < n: path[i][j] += path[i][j + 1]
                j -= 1
            i -= 1
        return path[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(1, 1))
    print(solution.uniquePaths(1, 3))
    print(solution.uniquePaths(3, 1))
    print(solution.uniquePaths(3, 3))
    print(solution.uniquePaths(3, 7))
