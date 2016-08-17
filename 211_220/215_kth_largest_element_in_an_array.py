#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def helper(nums, s, e):
            if s + k > e: return nums[s:e + 1]
            mid = (s + e) // 2
            merge = helper(nums, s, mid) + helper(nums, mid + 1, e)
            return (sorted(merge, reverse=True))[:k]

        if k == len(nums): return (sorted(nums))[0]
        return (helper(nums, 0, len(nums) - 1))[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findKthLargest([1], 1))
