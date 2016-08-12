#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.ret = nums[0]

        def binary_search(nums, start, end):
            if start == end: return nums[start]
            mid = (start + end) // 2
            if nums[start] > nums[mid]:
                return binary_search(nums, start, mid)
            else:
                if nums[end] > nums[start]: return nums[start]
                return binary_search(nums, mid + 1, end)

        return binary_search(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(solution.findMin([7, 0, 1, 2, 4, 5, 6]))
