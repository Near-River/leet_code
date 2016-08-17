#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value
appears at least twice in the array, and it should return false if every element is distinct.
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        i, j = 0, length - 1
        map = {}
        while i < j:
            if nums[i] in map: return True
            map[nums[i]] = True
            if nums[j] in map: return True
            map[nums[j]] = True
            i += 1
            j -= 1
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsDuplicate([3, 1]))
