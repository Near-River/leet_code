#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # solution one
        if not triangle: return 0

        def findMinSum(triangle, row, index, sum):
            if row == len(triangle): return sum
            sum += triangle[row][index]
            return min(findMinSum(triangle, row + 1, index, sum), findMinSum(triangle, row + 1, index + 1, sum))

        # return findMinSum(triangle=triangle, row=0, index=0, sum=0)

        # solution two: Dynamic Programming
        if not triangle: return 0
        dp = triangle[-1]
        r = len(triangle) - 2
        while r >= 0:
            nums = triangle[r]
            for i in range(r + 1):
                nums[i] += min(dp[i], dp[i + 1])
            dp = nums
            r -= 1
        return dp[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]))
