#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X
"""

from collections import deque


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return
        m, n = len(board), len(board[0])
        edgeO = set()
        for i in range(n):  # pretreatment: turn all 'O' on the edge to special character '#'
            if board[0][i] == 'O':
                board[0][i] = '#'
                edgeO.add((0, i))
            if board[m - 1][i] == 'O':
                board[m - 1][i] = '#'
                edgeO.add((m - 1, i))
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = '#'
                edgeO.add((i, 0))
            if board[i][n - 1] == 'O':
                board[i][n - 1] = '#'
                edgeO.add((i, n - 1))

        def bfs_fill(position):  # Breadth-first-search
            queue = deque([position])
            while queue:
                r, c = queue.popleft()
                if r - 1 >= 0 and board[r - 1][c] == 'O':
                    queue.append((r - 1, c))
                    board[r - 1][c] = '#'
                if r + 1 < m and board[r + 1][c] == 'O':
                    queue.append((r + 1, c))
                    board[r + 1][c] = '#'
                if c - 1 >= 0 and board[r][c - 1] == 'O':
                    queue.append((r, c - 1))
                    board[r][c - 1] = '#'
                if c + 1 < n and board[r][c + 1] == 'O':
                    queue.append((r, c + 1))
                    board[r][c + 1] = '#'

        for e in edgeO: bfs_fill(e)
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O': board[r][c] = 'X'
                if board[r][c] == '#': board[r][c] = 'O'


if __name__ == '__main__':
    solution = Solution()
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    print(solution.solve(board))
