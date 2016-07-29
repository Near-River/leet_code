#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.

Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]
"""

from copy import copy


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # solution one
        # ret, path = [], []
        # duplicated = set()
        #
        # def find_sums(target, index, path):
        #     if target == 0:
        #         _path = sorted(path)
        #         if _path not in ret:
        #             duplicated.add(path[0])
        #             ret.append(_path)
        #         return
        #     for i in range(index, len(candidates)):
        #         c = candidates[i]
        #         if c > target: continue
        #         if path == [] and c in duplicated: continue
        #         path.append(c)
        #         _path = copy(path)
        #         find_sums(target=target - c, index=i + 1, path=_path)
        #         path = path[:-1]

        # solution two
        ret, path = [], []
        candidates = sorted(candidates)

        def find_sums(target, index, path):
            if target == 0:
                ret.append(path)
                return
            prev = -1
            for i in range(index, len(candidates)):
                c = candidates[i]
                if c > target: break
                if prev != -1 and c == prev: continue
                path.append(c)
                _path = copy(path)
                find_sums(target=target - c, index=i + 1, path=_path)
                path = path[:-1]
                prev = c

        find_sums(target=target, index=0, path=path)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(solution.combinationSum2([4, 4, 2, 1, 4, 2, 2, 1, 3], 6))
