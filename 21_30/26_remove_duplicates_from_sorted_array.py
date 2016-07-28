#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1, 1, 2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         """
        # solution one
        length = len(nums)
        if length <= 1: return length

        n, i = nums[0], 1
        while i < length:
            if n == nums[i]:
                nums.remove(n)
                length -= 1
            else:
                n = nums[i]
                i += 1
        # return length

        # solution two
        # return len(set(nums))

        # solution three
        p1, p2 = 0, 1
        ret = 1
        for i in range(1, length):
            if nums[p1] != nums[p2]:
                ret += 1
                p1 = p2
            p2 += 1
        # return ret

        # solution four
        i = 0
        for j in range(1, length):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([]))
    print(solution.removeDuplicates([1, 1, 2]))
