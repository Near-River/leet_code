#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference
between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
"""

from collections import OrderedDict


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # solution one: Sliding Window + Bucket
        if k < 1 or t < 0: return False
        orderMap = OrderedDict()
        for i in range(len(nums)):
            m = nums[i] // max(1, t)
            for j in [m - 1, m, m + 1]:
                if j in orderMap and abs(nums[i] - orderMap[j]) <= t: return True
            orderMap[m] = nums[i]
            if i >= k: orderMap.popitem(last=False)
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsNearbyAlmostDuplicate([-1, -1], 1, 0))
