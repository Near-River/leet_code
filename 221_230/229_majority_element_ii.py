#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
The algorithm should run in linear time and in O(1) space.

Hint: How many majority elements could it possibly have?
"""

from collections import defaultdict


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # solution one: Hash Table
        # n = len(nums)
        # k = n // 3
        # ret = []
        # map = defaultdict(int)
        # for i in range(n):
        #     num = nums[i]
        #     map[num] += 1
        #     if map[num] > k:
        #         ret.append(num)
        #         map[num] = -n
        # return ret

        # solution two: Majority Voting Algorithm
        n, ret = len(nums), set()
        candidates = [0, 0]
        votes = [0, 0]
        for i in range(n):
            num = nums[i]
            if num == candidates[0]:
                votes[0] += 1
            elif num == candidates[1]:
                votes[1] += 1
            else:
                if votes[0] == 0:
                    candidates[0] = num
                    votes[0] += 1
                elif votes[1] == 0:
                    candidates[1] = num
                    votes[1] += 1
                else:
                    votes[0] -= 1
                    votes[1] -= 1
            pass
            # if 0 not in votes:
            #     if num == candidates[0]:
            #         votes[0] += 1
            #         votes[1] -= 1
            #     elif num == candidates[1]:
            #         votes[1] += 1
            #         votes[0] -= 1
            #     else:
            #         votes[0] -= 1
            #         votes[1] -= 1
            # elif votes[0] == votes[1]:
            #     candidates[0] = num
            #     votes[0] += 1
            # else:
            #     i, j = (0, 1) if votes[0] > 0 else (1, 0)
            #     if num == candidates[i]:
            #         votes[i] += 1
            #     else:
            #         candidates[j] = num
            #         votes[j] += 1
        votes = [0, 0]
        for i in range(n):
            if nums[i] == candidates[0]: votes[0] += 1
            if nums[i] == candidates[1]: votes[1] += 1
        for i in range(len(votes)):
            if votes[i] > len(nums) // 3: ret.add(candidates[i])
        return list(ret)


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([0, 0, 0]))
