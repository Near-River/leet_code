#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        异或运算：n ^ n = 0;       0 ^ x = x
        """
        # solution one: Bit Manipulation
        if not nums: return -1
        ret = nums[0]
        for i in range(1, len(nums)): ret ^= nums[i]
        # return ret

        # solution two: Hash Table
        d = {}
        for n in nums:
            if n not in d:
                d[n] = True
            else:
                del d[n]
        return (list(d.keys()))[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([1, 1, 2, 2, 3]))
