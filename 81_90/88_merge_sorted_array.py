#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        len1, len2 = len(nums1), len(nums2)
        if m < len1:
            for i in range(len1 - m): nums1.pop()
        else:
            m = len1
        if n < len2:
            for i in range(len2 - n): nums2.pop()
        else:
            n = len2
        p1, p2 = 0, 0
        if nums1:
            while p2 < n:
                if nums1[p1] <= nums2[p2]:
                    end = p1 + 1
                    while end < m and nums1[end] < nums2[p2]: end += 1
                    nums1.insert(end, nums2[p2])
                    p1 = end
                else:
                    nums1.insert(p1, nums2[p2])
                    p1 += 1
                m += 1
                p2 += 1
        else:
            for num in nums2: nums1.append(num)
        print(nums1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([1], 1, [], 0))
    print(solution.merge([0], 0, [1], 1))
    print(solution.merge([1, 3, 5, 7], 4, [0, 3, 4, 4, 4, 8], 9))
