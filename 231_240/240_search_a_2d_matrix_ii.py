#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

For example,
Consider the following matrix:
[
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])

        def list_binary_search(nums, s, e):
            if s > e: return False
            mid = (s + e) // 2
            if nums[mid] > target:
                return list_binary_search(nums, s, mid - 1)
            elif nums[mid] < target:
                return list_binary_search(nums, mid + 1, e)
            else:
                return True

        def binary_search(matrix, rs, re):
            mid = (rs + re) // 2
            if matrix[mid][0] < target:
                if matrix[mid][n - 1] >= target and list_binary_search(matrix[mid], 0, n - 1): return True
                if rs == re: return False
                if matrix[mid + 1][0] <= target and binary_search(matrix, mid + 1, re): return True
                if mid == rs: return False
                return binary_search(matrix, rs, mid - 1)
            elif matrix[mid][0] > target:
                if rs + 1 >= re: return False
                return binary_search(matrix, rs, mid - 1)
            else:
                return True

        return binary_search(matrix, 0, m - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchMatrix([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 5))
    print(solution.searchMatrix([[-1], [-1]], 0))
