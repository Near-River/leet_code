#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: list[int]
        :rtype: str
        """

        def sort(nums):
            for i in range(len(nums) - 1):
                for j in range(i, len(nums)):
                    if nums[i] + nums[j] < nums[j] + nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]

        nums = list(map(str, nums))
        sort(nums)
        ret = ''.join(nums)
        count = 0
        while count < len(ret) and ret[count] == '0': count += 1
        if count > 0: ret = '0' if count == len(ret) else ret[count:]
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestNumber([3, 30, 34, 5, 9]))
    print(solution.largestNumber([121, 12]))
