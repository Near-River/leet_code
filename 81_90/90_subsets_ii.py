#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.
Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1, 2, 2], a solution is:
[
    [2],
    [1],
    [1, 2, 2],
    [2, 2],
    [1, 2],
    []
]
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # solution one
        nums = sorted(nums)

        def find_all_subsets(nums, m):
            ret = []
            if m == 1:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i - 1]: continue
                    ret.append([nums[i]])
                return ret
            for i in range(len(nums) - m + 1):
                num = nums[i]
                if i > 0 and num == nums[i - 1]: continue
                for item in find_all_subsets(nums[i + 1:], m - 1):
                    ret.append([num] + item)
            return ret

        ret = [[], nums]
        for i in range(1, len(nums)):
            # find all subsets containing i elements
            ret.extend(find_all_subsets(nums, i))

        # return ret

        # solution two
        nums = sorted(nums)

        ret, duplicate = [[]], 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                duplicate += 1
            else:
                duplicate = 0
            for j in range(len(ret)):
                _lst = ret[j]
                if duplicate:
                    _len, flag = len(_lst), True
                    if _len < duplicate: continue
                    for k in range(duplicate):
                        if _lst[- 1 - k] != nums[i]:
                            flag = False
                            break
                    if flag: ret.append(_lst + [nums[i]])
                else:
                    ret.append(_lst + [nums[i]])
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsetsWithDup([1, 2, 2]))
    print(solution.subsetsWithDup([1, 2, 2, 2]))
