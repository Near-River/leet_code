#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1, 2, 3] have the following permutations:
    [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]
"""

from copy import copy


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []

        def permutation(nums):
            ret = []
            if len(nums) == 1: return [nums]
            for n in nums:
                _nums = copy(nums)
                _nums.remove(n)
                _ret = permutation(_nums)
                for _lst in _ret:
                    _lst.insert(0, n)
                    ret.append(_lst)
            return ret

        return permutation(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
    print(solution.permute([1, 2, 3, 4]))
