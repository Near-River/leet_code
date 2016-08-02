#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
    [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ]
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        nums = sorted(nums)

        def permutation(nums):
            ret = []
            if len(nums) == 1: return [nums]
            prev = -1
            for i in range(len(nums)):
                n = nums[i]
                if prev != -1 and nums[i] == nums[prev]: continue
                _ret = permutation(nums[:i] + nums[i + 1:])
                for _lst in _ret:
                    _lst.insert(0, n)
                    ret.append(_lst)
                prev = i
            return ret

        return permutation(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.permuteUnique([1, 1, 2]))
    print(solution.permuteUnique([1, 2, 2, 3]))
    a = [1, 2]
    b = [3, 4]
