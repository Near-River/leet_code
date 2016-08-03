#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a set of distinct integers, nums, return all possible subsets.
Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:
[
    [3],
    [1],
    [2],
    [1, 2, 3],
    [1, 3],
    [2, 3],
    [1, 2],
    []
]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Tags: Backtracking & Bit Manipulation
        # solution one: recursive
        def find_all_subsets(nums, m):
            ret = []
            if m == 1:
                for i in range(len(nums)): ret.append([nums[i]])
                return ret
            for i in range(len(nums) - m + 1):
                num = nums[i]
                for item in find_all_subsets(nums[i + 1:], m - 1):
                    item.insert(0, num)
                    ret.append(item)
            return ret

        ret = [[], nums]
        for i in range(1, len(nums)):
            # find all subsets containing i elements
            ret.extend(find_all_subsets(nums, i))
        # return ret

        # solution two: existed or not?
        ret = [[]]
        for i in range(len(nums)):
            num = nums[i]
            for j in range(len(ret)):
                _lst = ret[j]
                ret.append(_lst + [num])
        # return ret

        # solution three: bit manipulation
        bitMax, ret = 1 << len(nums), [[]]
        for i in range(1, bitMax):
            tempRet, currBit = [], i
            for j in range(len(nums)):
                if currBit & 1: tempRet.append(nums[j])
                currBit >>= 1
                if currBit == 0: break
            ret.append(tempRet)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1]))
    print(solution.subsets([1, 2, 3]))
    print(solution.subsets([1, 2, 3, 4]))
