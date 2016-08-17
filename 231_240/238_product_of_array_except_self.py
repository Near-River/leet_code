#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of
all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up: Could you solve it with constant space complexity?
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [1] * n
        for i in range(n - 1): output[i + 1] = output[i] * nums[i]
        product = 1
        for i in range(n - 1):
            product *= nums[n - 1 - i]
            output[n - i - 2] *= product
        return output


if __name__ == '__main__':
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4, 5]))
