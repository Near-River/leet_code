#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Follow up for "Unique Paths":
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.
[
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

The total number of unique paths is 2.
Note: m and n will be at most 100.
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
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
                if obstacleGrid[i][j] == 1:
                    path[i][j] = 0
                else:
                    if i + 1 < m: path[i][j] += path[i + 1][j]
                    if j + 1 < n: path[i][j] += path[i][j + 1]
                j -= 1
            i -= 1
        return path[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePathsWithObstacles([[0, 1, 0]]))
    print(solution.uniquePathsWithObstacles([[0], [1], [0]]))
    print(solution.uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))
