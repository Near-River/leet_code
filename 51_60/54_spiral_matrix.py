#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example    Given the following matrix:
[
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
]

You should return [1,2,3,6,9,8,7,4,5].
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        ret = []
        _m, _n, i = m, n, 0
        while _m > 0 and _n > 0:
            for j in range(_n - 1): ret.append(matrix[i][i + j])
            if _m == 1:
                ret.append(matrix[i][i + _n - 1])
                break
            for j in range(_m - 1): ret.append(matrix[i + j][n - i - 1])
            if _n == 1:
                ret.append(matrix[i + _m - 1][n - i - 1])
                break
            for j in range(_n - 1): ret.append(matrix[m - i - 1][n - j - i - 1])
            for j in range(_m - 1): ret.append(matrix[m - j - i - 1][i])
            _n -= 2
            _m -= 2
            i += 1
            if _m == 1 and _n == 1:
                ret.append(matrix[i][i])
                break
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))
    print(solution.spiralOrder([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]))
    print(solution.spiralOrder([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12],
        [13, 14, 15]
    ]))
