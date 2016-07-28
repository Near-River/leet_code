#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.

Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
    [
      [7],
      [2, 2, 3]
    ]
"""

from collections import OrderedDict
from copy import copy


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # Tags: Array & Backtracking

        # solution one
        # d = OrderedDict()
        # for c in candidates:
        #     if c > target: continue
        #     for i in range(1, target // c + 1):
        #         d[(c, i)] = c * i
        # # sorting dict by value
        # d = OrderedDict(sorted(d.items(), key=lambda x: x[1]))
        # ks, nums = list(d.keys()), list(d.values())
        # length, ret = len(nums), []
        #
        # def save_data(locations):
        #     """
        #     save data according to the locations corresponding to ks
        #     :param locations:
        #     """
        #     temp = []
        #     for j in locations:
        #         loop_val = ks[j][0]
        #         loop_times = ks[j][1]
        #         for k in range(loop_times):
        #             temp.append(loop_val)
        #     temp = sorted(temp)
        #     if temp not in ret: ret.append(temp)
        #
        # def find_sums(start, target, locations):
        #     """
        #     find all the combination numbers(allowing for repeated) sum up to the target
        #     :param start: start point
        #     :param target: sub - target value
        #     :param locations: recording the combination numbers location
        #     """
        #     # print(start, target, locations)
        #     _locations = copy(locations)
        #     for i in range(start, length):
        #         n = nums[i]
        #         left = target - n
        #         if left == 0 and locations == []:
        #             save_data([i])
        #             continue
        #         if left < n: continue
        #         locations.append(i)
        #
        #         if left in nums[i + 1:]:
        #             # save the data
        #             idx = (nums[i + 1:]).index(left) + i + 1
        #             locations.append(idx)
        #             save_data(locations)
        #             locations = locations[:-1]
        #             while idx < length - 1 and left in nums[idx + 1:]:
        #                 idx = (nums[idx + 1:]).index(left) + idx + 1
        #                 locations.append(idx)
        #                 save_data(locations)
        #                 locations = locations[:-1]
        #         locations = copy(_locations)
        #         locations.append(i)
        #         find_sums(i + 1, left, locations)  # recursion
        #         locations = copy(_locations)
        #
        # find_sums(0, target, [])
        # return sorted(ret)

        # solution two
        ret, path = [], []
        sorted(candidates)

        def find_sums2(target, index, path):
            if target == 0:
                ret.append(path)
                return
            prev = -1
            for i in range(index, len(candidates)):
                if candidates[i] > target: break
                if prev != -1 and prev == candidates[i]: continue
                path.append(candidates[i])
                find_sums2(target=target - candidates[i], index=i, path=path)
                path = path[:-1]
                prev = candidates[i]

        find_sums2(target=target, index=0, path=path)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([2, 3, 6, 7], 7))
    print(solution.combinationSum([1, 1], 2))
    print(solution.combinationSum([1, 2], 3))
    print(solution.combinationSum([7, 3, 2], 18))
