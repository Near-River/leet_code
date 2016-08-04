#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # solution one
        m, n = len(matrix), len(matrix[0])
        rows, columns = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)
        for i in rows:
            for j in range(n): matrix[i][j] = 0
        for i in columns:
            for j in range(m): matrix[j][i] = 0

        # solution two: reuse the constant space
        m, n = len(matrix), len(matrix[0])
        zeroRow, zeroColumn = False, False
        if 0 in matrix[0]: zeroColumn = True
        for i in range(m):
            if matrix[i][0] == 0:
                zeroRow = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m): matrix[i][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n): matrix[i][j] = 0
        if zeroRow:
            for i in range(m): matrix[i][0] = 0
        if zeroColumn:
            for j in range(n): matrix[0][j] = 0


if __name__ == '__main__':
    solution = Solution()
    solution.setZeroes([
        [1, 2, 3, 0, 5],
        [0, 7, 0, 9, 10],
        [11, 12, 13, 14, 15]
    ])
