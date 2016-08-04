#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:
[
    [2, 4],
    [3, 4],
    [2, 3],
    [1, 2],
    [1, 3],
    [1, 4],
]
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # solution one
        nums = []
        for i in range(1, n + 1): nums.append(i)

        def find_all_combinations(nums, m):
            ret = []
            if m == 1:
                for i in range(len(nums)): ret.append([nums[i]])
                return ret
            for i in range(len(nums) - m + 1):
                for item in find_all_combinations(nums[i + 1:], m - 1):
                    ret.append([nums[i]] + item)
            return ret

        # find all possible combinations of k numbers
        # return find_all_combinations(nums, k)

        # solution two: Time Limit Exceeded
        nums = []
        for i in range(1, n + 1): nums.append(i)
        temp, ret = [[]], []
        for num in nums:
            for j in range(len(temp)):
                _lst = temp[j]
                if len(_lst) <= k - 1:
                    if len(_lst) == k - 1:
                        ret.append(_lst + [num])
                    temp.append(_lst + [num])
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))
