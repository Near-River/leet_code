#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ISuppose a sorted array is rotated at some pivot(枢) unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binary_search(nums, start):
            length = len(nums)
            if length == 0: return -1
            if length == 1: return start if target == nums[0] else -1
            mid = (length - 1) // 2
            if nums[mid] > target:
                return binary_search(nums[0:mid], start)
            elif nums[mid] < target:
                return binary_search(nums[mid + 1:], start + mid + 1)
            else:
                return start + mid

        pivot = []
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]: pivot.append(i + 1)
        if not pivot: return binary_search(nums, 0)
        start = i = 0
        while i < len(pivot):
            ret = binary_search(nums[start:pivot[i]], start)
            if ret != -1: return ret
            start = pivot[i]
            i += 1
        return binary_search(nums[pivot[i - 1]:], start)


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([1, 3], 0))
