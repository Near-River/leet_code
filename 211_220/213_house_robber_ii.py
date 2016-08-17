#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not
get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the
neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

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
        if n <= 2: return 0 if n == 0 else max(nums)
        a, b, c = 0, nums[0], 0
        a2, b2, c2 = 0, nums[1], 0
        for i in range(1, n - 1):
            c = max(a + nums[i], b)
            c2 = max(a2 + nums[i + 1], b2)
            a, b = b, c
            a2, b2 = b2, c2
        return max(c, c2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([2, 3, 2]))
    print(solution.rob([1, 1, 1]))
    print(solution.rob([1, 2, 1, 1]))
