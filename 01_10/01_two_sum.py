#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.

Given nums = [2, 7, 11, 15], target = 9,    Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

from itertools import combinations


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {k: v for k, v in enumerate(nums)}

        # Solution one - 1
        for k1, k2 in combinations(d, 2):
            if d[k1] + d[k2] == target:
                return [k1, k2]

        # Solution one - 2
        for i in d.keys():
            for j in d.keys():
                if i == j:
                    continue
                if d[i] + d[j] == target:
                    return [i, j]

        # Solution two
        i = 0
        for v in d.values():
            if target - v in d.values():
                idx = list(d.values()).index(target - v)
                if i != idx:
                    return [min(i, idx), max(i, idx)]
            i += 1

        # Solution three
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in dict:
                return (dict[target - x], i)
            dict[x] = i


if __name__ == '__main__':
    lst = [3, 2, 4]
    solution = Solution()
    result = solution.twoSum(nums=lst, target=6)
    print(result)
