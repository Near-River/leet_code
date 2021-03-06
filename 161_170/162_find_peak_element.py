#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A peak element is an element that is greater than its neighbors.
Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that num[-1] = num[n] = -∞.
For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

Note:
Your solution should be in logarithmic complexity.
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, e = 0, len(nums) - 1
        while s <= e:
            if s == e: return s
            mid = (s + e) // 2
            if nums[mid] < nums[mid + 1]:
                s = mid + 1
            else:
                e = mid


if __name__ == '__main__':
    solution = Solution()
    print(solution.findPeakElement([1, 2, 3, 1]))
