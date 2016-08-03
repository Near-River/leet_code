#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        # solution one
        # def binary_search(nums, start):
        #     length = len(nums)
        #     if length == 0: return False
        #     if length == 1: return True if target == nums[0] else False
        #     mid = (length - 1) // 2
        #     if nums[mid] > target:
        #         return binary_search(nums[0:mid], start)
        #     elif nums[mid] < target:
        #         return binary_search(nums[mid + 1:], start + mid + 1)
        #     else:
        #         return True
        #
        # pivot = []
        # count, new_nums = 0, []
        # for i in range(len(nums) - 1):
        #     if nums[i] != nums[i + 1]:
        #         new_nums.append(nums[i])
        #         count += 1
        #         if nums[i] > nums[i + 1]: pivot.append(count)
        # if nums: new_nums.append(nums[-1])
        # print(new_nums, pivot)
        # if not pivot: return binary_search(new_nums, 0)
        # start = i = 0
        # while i < len(pivot):
        #     ret = binary_search(new_nums[start:pivot[i]], start)
        #     if ret: return True
        #     start, i = pivot[i], i + 1
        # return binary_search(new_nums[pivot[i - 1]:], start)

        # solution two
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target: return True
            if nums[start] > nums[mid]:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            elif nums[start] < nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                start += 1
        return False


if __name__ == '__main__':
    solution = Solution()
    solution = Solution()
    print(solution.search([3, 1], 1))
    print(solution.search([1, 1, 3, 1], 1))
    print(solution.search([1, 2, 2, 2, 0, 1, 1], 0))
