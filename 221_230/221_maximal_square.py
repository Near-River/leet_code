#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4.
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # solution one
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        ret = 0
        heights = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[i][j] = heights[i - 1][j] + 1 if i > 0 else 1
        for height in heights:
            height.append(0)
            stack, i = [], 0
            while i < len(height):
                if not stack or height[i] >= height[stack[-1]]:
                    stack.append(i)
                    i += 1
                else:
                    idx = stack.pop()
                    rn = i
                    ln = -1 if not stack else stack[-1]
                    ret = max(ret, min(height[idx], rn - ln - 1) ** 2)
        # return ret

        # solution two: Dynamic Programming
        """
        dp(i,j) represents the side length of the maximum square whose bottom right corner is the cell with
        index (i,j) in the original matrix. Starting from index (0,0), for every 1 found in the original matrix,
        we update the value of the current element as:
            dp(i, j)=min(dp(i−1, j), dp(i−1, j−1), dp(i, j−1))+1.
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)
        ret = 0
        for i in range(m):
            prev = dp[0]
            for j in range(n):
                temp = dp[j + 1]
                if matrix[i][j] == '1':
                    dp[j + 1] = min(dp[j], dp[j + 1], prev) + 1
                    ret = max(ret, dp[j + 1] ** 2)
                else:
                    dp[j + 1] = 0
                prev = temp
        return ret


if __name__ == '__main__':
    solution = Solution()
    lst = ["10100", "10111", "11111", "10010"]
    matrix = []
    for l in lst: matrix.append(list(l))
    print(solution.maximalSquare(matrix))
