#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length < 2: return
        i = length - 2
        while i >= 0:
            if nums[i] < nums[i + 1]: break
            i -= 1
        if i >= 0:
            j = length - 1
            while nums[j] <= nums[i]: j -= 1
            nums[j], nums[i] = nums[i], nums[j]
            temp = sorted(nums[i + 1:])
            for k in range(len(temp)): nums[k + i + 1] = temp[k]
        else:
            temp = sorted(nums)
            for k in range(length): nums[k] = temp[k]
        # print(nums)

if __name__ == '__main__':
    solution = Solution()
    print(solution.nextPermutation([1, 2, 3]))
    print(solution.nextPermutation([3, 2, 1]))
    print(solution.nextPermutation([1, 2, 6, 5, 4, 3]))
    print(solution.nextPermutation([2, 2, 6, 5, 4, 2]))
    print(solution.nextPermutation([5, 10, 9, 8, 3, 2, 1]))
    print(solution.nextPermutation([5, 4, 3, 2, 1]))
    print(solution.nextPermutation([4, 2, 0, 2, 3, 2, 0]))
