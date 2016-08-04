#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        i = m - 1
        while i >= 0:
            j = n - 1
            while j >= 0:
                if i + 1 < m and j + 1 < n:
                    grid[i][j] += min(grid[i][j + 1], grid[i + 1][j])
                elif i + 1 < m and j + 1 >= n:
                    grid[i][j] += grid[i + 1][j]
                elif i + 1 >= m and j + 1 < n:
                    grid[i][j] += grid[i][j + 1]
                j -= 1
            i -= 1
        return grid[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minPathSum([
        [3, 7, 9],
        [11, 5, 1],
        [2, 4, 0],
    ]))
    print(solution.minPathSum([[1, 2], [5, 6], [1, 1]]))
