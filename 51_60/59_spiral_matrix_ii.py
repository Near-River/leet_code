#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example, Given n = 3,
You should return the following matrix:
[
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
]
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = []
        for i in range(n):
            matrix.append([])
            for j in range(n):
                matrix[i].append(0)
        loop, _n = n // 2, n
        count = 1
        for i in range(loop):
            for j in range(_n - 1):
                matrix[i][i + j] = count + j
                matrix[i + j][n - i - 1] = count + j + _n - 1
                matrix[n - i - 1][n - 1 - i - j] = count + j + 2 * (_n - 1)
                matrix[n - 1 - i - j][i] = count + j + 3 * (_n - 1)
            count += 4 * (_n - 1)
            _n -= 2
        if n % 2 == 1: matrix[loop][loop] = n * n
        return matrix


if __name__ == '__main__':
    solution = Solution()
    solution.generateMatrix(0)
    print(solution.generateMatrix(1))
    print(solution.generateMatrix(2))
    print(solution.generateMatrix(3))
    print(solution.generateMatrix(4))
