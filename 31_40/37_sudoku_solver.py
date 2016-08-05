#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DWrite a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'.
You may assume that there will be only one unique solution.

Rules:
    Each row must have the numbers 1-n occuring just once.
    Each column must have the numbers 1-n occuring just once.
    And the numbers 1-n must occur just once in each of the n sub-boxes of the grid.
"""
from math import sqrt


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = int(sqrt(n))
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        def validateNumber(row, col, num):
            if num in board[row]: return False
            for r in range(n):
                if board[r][col] == num: return False
            x, y = row // m, col // m
            for r in range(x * m, x * m + m):
                for c in range(y * m, y * m + m):
                    if board[r][c] == num: return False
            return True

        def fillSudoku(start):
            i, j = start
            flag = False
            while i < n:  # search the next missing number's location
                while j < n:
                    if board[i][j] == '.':
                        flag = True
                        break
                    j += 1
                if flag: break
                j, i = 0, i + 1
            if not flag: return True
            row, col = i, j
            if col == n - 1:
                row += 1
                col = 0
            else:
                col += 1
            for num in nums:  # validate the number
                if not validateNumber(i, j, num): continue
                board[i][j] = num
                if fillSudoku((row, col)): return True
            board[i][j] = '.'

        fillSudoku(start=(0, 0))
        # for i in board:
        #     print(i)


if __name__ == '__main__':
    solution = Solution()
    lst = ["..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6",
           "...2759.."]
    board = []
    for s in lst: board.append(list(s))
    print(solution.solveSudoku(board))
