#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3
Your function should return length = 2, with the first two elements of nums being 2.
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # solution one
        length = len(nums)
        if length < 1: return length

        i, j = 0, length - 1
        while i <= j:
            if nums[i] == val or nums[j] == val:
                while nums[i] == val or nums[j] == val:
                    nums.remove(val)
                    if nums == []: return 0
                    j -= 1
            i += 1
            j -= 1
        # return len(nums)

        # solution two
        length = len(nums)
        i = 0
        for j in range(length):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeElement(nums=[3, 2, 2, 3], val=3))
    print(solution.removeElement(nums=[1], val=1))
    print(solution.removeElement(nums=[3, 3], val=3))
