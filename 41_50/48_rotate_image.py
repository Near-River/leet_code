#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Follow up: Could you do this in-place?
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n <= 1: return
        loop_times, m = n // 2, n
        for loop in range(loop_times):
            for i in range(m - 1):
                x, y = loop, loop + i
                trade = matrix[x][y]
                x, y = y, n - x - 1
                while x != loop or y != loop + i:
                    item = matrix[x][y]
                    matrix[x][y] = trade
                    trade = item
                    x, y = y, n - x - 1
                matrix[x][y] = trade
            m -= 2

        # for lst in matrix:
        #     print(lst)


if __name__ == '__main__':
    solution = Solution()
    print(solution.rotate([[1, 2], [3, 4]]))
    print(solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(solution.rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
