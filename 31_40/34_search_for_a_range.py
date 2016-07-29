#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a sorted array of integers, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binary_search(nums, start):
            """
            :param nums: a sorted array of integers
            :param start: the start position for searching
            :return: the target position found in the array
            """
            if nums == []: return [-1, -1]
            length = len(nums)
            mid = (length - 1) // 2
            mid_val = nums[mid]
            if mid_val < target:
                return binary_search(nums[mid + 1:], start + mid + 1)
            elif mid_val > target:
                return binary_search(nums[:mid], start)
            else:
                i = j = mid
                while i >= 0 and j < length:
                    if nums[i] == target or nums[j] == target:
                        if nums[i] == target: i -= 1
                        if nums[j] == target: j += 1
                    else:
                        break
                if j < length and nums[j] == target: j += 1
                return [start + i + 1, start + j - 1]

        return binary_search(nums=nums, start=0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
    print(solution.searchRange(nums=[0, 0, 2, 3, 4, 4, 4, 5], target=5))
