#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

For example:
A = [2, 3, 1, 1, 4], return true.
A = [3, 2, 1, 0, 4], return false.
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # length = len(nums)
        #
        # def greedy_jump(index):
        #     if index >= length - 1: return True
        #     jumps = nums[index]
        #     if jumps == 0: return False
        #     while jumps >= 1:
        #         if greedy_jump(index + jumps): return True
        #         jumps -= 1
        #     return False
        #
        # return greedy_jump(0)

        # solution one - 1
        length = len(nums)
        index, max_walks = 0, nums[0]
        while True:
            if index + max_walks >= length - 1: return True
            if max_walks == 0: return False
            n, max_walks = max_walks, 0
            for i in range(1, n + 1): max_walks = max(max_walks, nums[index + i] - n + i)
            index += n

        # solution one - 2
        length = len(nums)
        if length <= 1: return True
        max_walks = nums[0]
        for i in range(1, length):
            if max_walks == 0: return False
            max_walks -= 1
            if nums[i] > max_walks: max_walks = nums[i]
            if max_walks + i >= length - 1: return True

        # solution one - 3
        i = lastPos = len(nums) - 1
        while i >= 0:
            if i + nums[i] >= lastPos: lastPos = i
            i -= 1
        return lastPos == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.canJump([2]))
    print(solution.canJump([2, 5, 0, 0]))
    print(solution.canJump([2, 3, 1, 1, 4]))
    print(solution.canJump([3, 2, 1, 0, 4]))
