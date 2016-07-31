#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Here are few examples.
[1, 3, 5, 6], 5 → 2
[1, 3, 5, 6], 2 → 1
[1, 3, 5, 6], 7 → 4
[1, 3, 5, 6], 0 → 0
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # def binary_search(nums, start):
        #     length = len(nums)
        #     if length == 0: return start
        #     if length == 1: return start if target <= nums[0] else start + 1
        #
        #     mid = (length - 1) // 2
        #     if nums[mid] > target:
        #         return binary_search(nums[0:mid], start)
        #     elif nums[mid] < target:
        #         return binary_search(nums[mid + 1:], start + mid + 1)
        #     else:
        #         return start + mid

        def binary_search2(nums, start):
            mid = (len(nums) - 1) // 2
            if nums[mid] > target:
                return binary_search2(nums[0:mid], start) if mid > 0 else start
            elif nums[mid] < target:
                return binary_search2(nums[mid + 1:], start + mid + 1) if mid + 1 < len(nums) else start + 1
            else:
                return start + mid

        return binary_search2(nums, 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1, 3, 5, 6], 5))
    print(solution.searchInsert([1, 3, 5, 6], 2))
    print(solution.searchInsert([1, 3, 5, 6], 7))
    print(solution.searchInsert([1, 3, 5, 6], 0))
    print(solution.searchInsert([1, 3, 5, 6, 9], 0))
