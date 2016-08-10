#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution one: Time Limit Exceeded
        # if not nums: return -1
        # d = {}
        # for n in nums:
        #     if n not in d.keys():
        #         d[n] = 1
        #     else:
        #         d[n] += 1
        #         if d[n] == 3: del d[n]
        # return (list(d.keys()))[0]

        # solution two
        # ret = 0
        # for i in range(32):
        #     count, base = 0, 1 << i
        #     for n in nums:
        #         if n & base: count += 1
        #     if count % 3: ret |= base

        binary = ''
        for i in range(32):
            count, base = 0, 1 << i
            for n in nums:
                if n & base: count += 1
            if count % 3:
                binary += '1'
            else:
                binary += '0'
        ret = int(binary[::-1], 2)
        if binary[-1] == '1':  # turn 32 unsigned integer to signed integer
            ret = -((ret - 1) ^ 0xffffffff)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([1, 1, 1, 5, 3, 3, 3, 2, 2, 2]))
    print(solution.singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]))
