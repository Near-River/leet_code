#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return
[
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [[1 for j in range(i + 1)] for i in range(numRows)]
        for r in range(3, numRows + 1):
            # calculate pascal[r-1] based on pascal[r-2]
            # for c in range(1, r - 1):
            #     pascal[r - 1][c] = pascal[r - 2][c - 1] + pascal[r - 2][c]
            for c in range(1, 1 + (r - 1) // 2):
                pascal[r - 1][c] = pascal[r - 1][r - 1 - c] = pascal[r - 2][c - 1] + pascal[r - 2][c]
        return pascal


if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(1))
    print(solution.generate(3))
    print(solution.generate(4))
    print(solution.generate(5))
