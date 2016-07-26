#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
    nums1 = [1, 3]
    nums2 = [2]
    The median is 2.0

Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    The median is (2 + 3)/2 = 2.5
"""

from collections import deque


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged, left, right = deque(), deque(nums1), deque(nums2)
        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())
        merged.extend(left if left else right)
        length = len(merged)
        if length % 2 == 1:
            return merged[length // 2]
        else:
            half = length // 2
            return (merged[half - 1] + merged[half]) / 2


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 3], [2]))
    print(solution.findMedianSortedArrays([1, 2], [3, 4]))
