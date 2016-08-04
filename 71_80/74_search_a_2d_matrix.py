#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

For example,
Consider the following matrix:
[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # solution one
        def list_binary_search(nums, target):
            n = len(nums)
            if n == 0: return False
            if n == 1: return target == nums[0]
            mid = n // 2
            if nums[mid] > target:
                return list_binary_search(nums[:mid], target)
            elif nums[mid] < target:
                return list_binary_search(nums[mid + 1:], target)
            else:
                return True

        def matrix_binary_search(matrix, target):
            m = len(matrix)
            if m == 0: return False
            if m == 1: return list_binary_search(matrix[0], target)
            mid = m // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return list_binary_search(matrix[mid], target)
            elif matrix[mid][0] > target:
                return matrix_binary_search(matrix[:mid], target)
            else:
                return matrix_binary_search(matrix[mid + 1:], target)

        # return matrix_binary_search(matrix, target)

        # solution two
        nums = []
        for columns in matrix: nums.extend(columns)
        return list_binary_search(nums, target)


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchMatrix([[1]], 0))
