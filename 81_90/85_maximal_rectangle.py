#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 6.
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        # Array & Hash Table & Stack & Dynamic Programming
        """
        Reference the Largest_Rectangle_In_Histogram problem
        'Draw' the linear maps for each row and then calculate the largest rectangle respectively.
        """
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        heights = [list(map(int, matrix[0]))]
        heights.extend([[0 for i in range(n)] for j in range(m - 1)])
        for r in range(1, m):
            for c in range(n):
                if matrix[r][c] == '1': heights[r][c] = heights[r - 1][c] + 1
        maxArea = 0
        for r in range(m):
            height = heights[r]
            height.append(0)
            stack, i = [], 0
            while i < n + 1:
                if not stack or height[i] >= height[stack[-1]]:
                    stack.append(i)
                    i += 1
                else:
                    idx = stack.pop()
                    rn = i
                    ln = -1 if not stack else stack[-1]
                    maxArea = max(maxArea, height[idx] * (rn - ln - 1))
        return maxArea


if __name__ == '__main__':
    solution = Solution()
    lst = ["10100", "10111", "11111", "10010"]
    matrix = []
    for l in lst: matrix.append(list(l))
    print(solution.maximalRectangle(matrix))
