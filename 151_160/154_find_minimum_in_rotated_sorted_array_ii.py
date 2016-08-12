#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?

Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.
The array may contain duplicates.
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            if start == end: return nums[start]
            mid = (start + end) // 2
            if nums[end] > nums[mid]:
                end = mid
            elif nums[end] < nums[mid]:
                start = mid + 1
            else:
                end -= 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMin([3, 1]))
    print(solution.findMin([1, 1, 3, 1]))
    print(solution.findMin([1, 2, 2, 2, 0, 1, 1]))
    print(solution.findMin([1, 1, 2, 0, 0, 1]))
