#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution one
        if len(nums) == 1: return nums[0]
        d = {}
        size = len(nums) // 2
        for n in nums:
            if n in d:
                d[n] += 1
                if d[n] > size: return n
            else:
                d[n] = 1

        # solution two
        count = 0
        ret = nums[0]
        for i in range(len(nums)):
            if count == 0 or ret == nums[i]:
                ret = nums[i]
                count += 1
            else:
                count -= 1
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([1]))
    print(solution.majorityElement([3, 2, 3]))
