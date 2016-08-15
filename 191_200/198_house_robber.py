#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(1, n):
            dp[i + 1] = max(dp[i - 1] + nums[i], dp[i])
        # return dp[-1]

        # optimization
        n = len(nums)
        if n < 2: return 0 if n == 0 else nums[0]
        a, b, c = 0, nums[0], 0
        for i in range(1, n):
            c = max(a + nums[i], b)
            a, b = b, c
        return c


if __name__ == '__main__':
    solution = Solution()
