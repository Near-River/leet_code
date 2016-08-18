#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        ret = []
        n, start = len(nums), 0
        for i in range(1, n):
            if nums[i] != nums[start] + i - start:
                if i == start + 1:
                    ret.append("%d" % (nums[start]))
                else:
                    ret.append("%d->%d" % (nums[start], nums[i - 1]))
                start = i
        if n == start + 1:
            ret.append("%d" % (nums[start]))
        else:
            ret.append("%d->%d" % (nums[start], nums[-1]))
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.summaryRanges([0, 1, 2, 4, 5, 7]))
