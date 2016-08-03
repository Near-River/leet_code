#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         """
        length = len(nums)
        if length <= 2: return length
        p1, p2 = 0, 1
        ret, twice = 1, False
        while p2 < length:
            if nums[p1] != nums[p2]:
                twice = False
            elif not twice:
                twice = True
            else:
                while p2 < length and nums[p2] == nums[p1]: p2 += 1
                if p2 >= length: break
                twice = False
            nums[ret] = nums[p2]  # update nums
            ret += 1
            p1, p2 = p2, p2 + 1

        # print('nums', nums[:ret])
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([]))
    print(solution.removeDuplicates([1, 1, 2]))
    print(solution.removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(solution.removeDuplicates([1, 1, 1, 1, 3, 3]))
