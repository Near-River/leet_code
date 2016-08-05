#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2, 3, 1, 1, 4]
The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note: You can assume that you can always reach the last index.
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution one
        # length, MAX_INT = len(nums), 2147483647
        # minSteps = [0 for i in range(length)]
        # i = length - 2
        # while i >= 0:
        #     jumps = nums[i]
        #     lst = []
        #     for j in range(jumps):
        #         if i + j + 1 >= length:break
        #         lst.append(minSteps[i + j + 1])
        #     if lst:
        #         minSteps[i] = min(lst) + 1
        #     else:
        #         minSteps[i] = MAX_INT
        #     i -= 1
        # return minSteps[0]

        # solution two
        length = len(nums)
        maxArrival = []
        for i in range(length): maxArrival.append(i + nums[i])
        steps = 0
        aim, flag = length - 1, True
        while aim:
            for idx in range(length):
                if maxArrival[idx] >= aim:
                    aim = idx
                    break
            steps += 1

        # return steps

        # solution three: Dynamic Programming
        ret = 0
        lastMax, currMax = 0, 0
        for i in range(len(nums)):
            if lastMax < i:
                lastMax = currMax
                ret += 1
            currMax = max(currMax, nums[i] + i)

        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.jump([2]))
    print(solution.jump([2, 3, 1, 1, 4]))
    print(solution.jump([2, 3, 0, 1, 4]))
    print(solution.jump([1, 2, 0, 1]))
