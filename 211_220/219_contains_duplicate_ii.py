#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the difference between i and j is at most k.
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if k < 1 or n < 2: return False
        map = {}
        for i in range(n):
            num = nums[i]
            if num in map:
                if i - map[num] <= k: return True
            map[num] = i

        return False


if __name__ == '__main__':
    solution = Solution()
