#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area, maxArea = 0, -1
        first, last = 0, len(height) - 1
        while first < last:
            if height[first] > height[last]:
                area = (last - first) * height[last]
                last -= 1
            else:
                area = (last - first) * height[first]
                first += 1
            if area > maxArea:  maxArea = area
        return maxArea


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1, 1]))
    print(solution.maxArea([0, 2]))
    print(solution.maxArea([2, 1]))
