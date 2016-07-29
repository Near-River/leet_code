#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3, and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        if nums == []: return 1

        def binary_search(nums):
            """
            search for the first non-negative value, if not exist, return -1
            :param nums: sorted integer array
            :return: the first non-negative value's index, -1 is returned if the value not exist.
            """
            length = len(nums)
            if length == 1: return -1 if nums[0] < 0 else nums[0]
            mid = (length - 1) // 2
            if nums[mid] < 0:
                return binary_search(nums[mid + 1:])
            else:
                return binary_search(nums[:mid + 1])

        curr = binary_search(nums)
        if curr >= 2 or curr < 0:
            return 1
        else:
            idx = nums.index(curr)
            if idx == len(nums) - 1: return curr + 1
            for j in range(idx + 1, len(nums)):
                if nums[j] >= curr + 2: return curr + 1
                curr = nums[j]
            return curr + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.firstMissingPositive([1, 2, 0]))
    print(solution.firstMissingPositive([3, 4, -1, 1]))
    print(solution.firstMissingPositive([1, 2, 3]))
