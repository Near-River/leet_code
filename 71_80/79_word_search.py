#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        len1, len2 = len(board), len(board[0])

        def find_word(word, duplicate):
            """
            :param duplicate: save all the passed cells location
            :return:
            """
            # search word from four direction
            i, j = duplicate[-1]
            if i - 1 >= 0 and (i - 1, j) not in duplicate:
                if board[i - 1][j] == word[0]:
                    if len(word) == 1: return True
                    if find_word(word[1:], duplicate + [(i - 1, j)]): return True
            if j - 1 >= 0 and (i, j - 1) not in duplicate:
                if board[i][j - 1] == word[0]:
                    if len(word) == 1: return True
                    if find_word(word[1:], duplicate + [(i, j - 1)]): return True
            if j + 1 < len2 and (i, j + 1) not in duplicate:
                if board[i][j + 1] == word[0]:
                    if len(word) == 1: return True
                    if find_word(word[1:], duplicate + [(i, j + 1)]): return True
            if i + 1 < len1 and (i + 1, j) not in duplicate:
                if board[i + 1][j] == word[0]:
                    if len(word) == 1: return True
                    if find_word(word[1:], duplicate + [(i + 1, j)]): return True
            return False

        for i in range(len1):
            for j in range(len2):
                ch = board[i][j]
                if ch != word[0]: continue
                if len(word) == 1: return True
                if find_word(word[1:], [(i, j)]): return True

        return False


if __name__ == '__main__':
    solution = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    print(solution.exist(board, 'ABCCED'))
    print(solution.exist(board, 'SEE'))
    print(solution.exist(board, 'ABCB'))
    print(solution.exist([['a', 'a']], 'a'))
