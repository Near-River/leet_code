#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which
the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ret = n + 1
        _sum = start = 0
        for i in range(n):
            _sum += nums[i]
            while _sum >= s:
                ret = min(ret, i - start + 1)
                _sum -= nums[start]
                start += 1
        return ret if ret <= n else 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
