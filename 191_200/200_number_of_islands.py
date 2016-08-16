#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:
11110
11010
11000
00000
Answer: 1

Example 2:
11000
11000
00100
00011
Answer: 3
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        board = [['0'] * (n + 2)]
        for l in grid: board.append(['0'] + l + ['0'])
        board.append(['0'] * (n + 2))
        ret = 0

        def bfs(location):
            stack = [location]
            while stack:
                x, y = stack.pop()
                if board[x - 1][y] == '1':
                    stack.append((x - 1, y))
                    board[x - 1][y] = '0'
                if board[x][y - 1] == '1':
                    stack.append((x, y - 1))
                    board[x][y - 1] = '0'
                if board[x + 1][y] == '1':
                    stack.append((x + 1, y))
                    board[x + 1][y] = '0'
                if board[x][y + 1] == '1':
                    stack.append((x, y + 1))
                    board[x][y + 1] = '0'

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if board[i][j] == '1':
                    bfs((i, j))
                    ret += 1
        return ret


if __name__ == '__main__':
    solution = Solution()
    lst = ['11110', '11010', '11000', '00000']
    grid = []
    for l in lst: grid.append(list(l))
    print(solution.numIslands(grid))
