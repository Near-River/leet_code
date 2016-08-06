#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] == 0:
                if nums[j] == 2: j -= 1
                i += 1
            elif nums[i] == 1:
                if nums[j] == 2:
                    j -= 1
                elif nums[j] == 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                else:
                    temp = i + 1
                    while temp < j:
                        if nums[temp] != 1: break
                        temp += 1
                    if temp >= j: break
                    if nums[temp] == 0:
                        nums[i], nums[temp] = nums[temp], nums[i]
                        i += 1
                    else:
                        nums[temp], nums[j] = nums[j], nums[temp]
                        j -= 1
            else:
                if nums[j] == 2:
                    if i < j - 1: nums[i], nums[j - 1] = nums[j - 1], nums[i]
                elif nums[j] == 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                j -= 1

        # print(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortColors([0]))
    print(solution.sortColors([2, 1]))
    print(solution.sortColors([2, 1, 0]))
    print(solution.sortColors([2, 1, 1, 1, 1, 0, 2, 1, 1, 1, 0]))
    print(solution.sortColors([2, 0, 1, 0, 2, 1, 0]))
