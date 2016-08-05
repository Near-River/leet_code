#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

Rules:
    Each row must have the numbers 1-n occuring just once.
    Each column must have the numbers 1-n occuring just once.
    And the numbers 1-n must occur just once in each of the n sub-boxes of the grid.
"""
from math import sqrt


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = len(board)
        # Each row must have the numbers 1-n occuring just once.
        for r in range(n):
            row_lst = []
            for c in range(n):
                if board[r][c] == '.': continue
                if board[r][c] in row_lst: return False
                row_lst.append(board[r][c])
        # Each column must have the numbers 1-n occuring just once.
        for c in range(n):
            col_lst = []
            for r in range(n):
                if board[r][c] == '.': continue
                if board[r][c] in col_lst: return False
                col_lst.append(board[r][c])
        # And the numbers 1-n must occur just once in each of the n sub-boxes of the grid.
        m = int(sqrt(n))
        for i in range(n):
            mod, left = i // m, i % m
            sub_board = []
            for j in range(mod * m, mod * m + m):
                for k in range(left * m, left * m + m):
                    if board[j][k] == '.': continue
                    if board[j][k] in sub_board: return False
                    sub_board.append(board[j][k])
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValidSudoku(
        [".87654321", "2........", "3........", "4........", "5........", "6........", "7........", "8........",
         "9........"]))
    print(solution.isValidSudoku(
        [".21......", "....6....", "......7..", "....5....", "..5......", "......3..", ".........", "3...8.1..",
         "........8"]))
