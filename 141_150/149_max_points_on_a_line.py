#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""

from collections import defaultdict


# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        ret = 0
        rmap, cmap = defaultdict(int), defaultdict(int)
        for point in points:
            x, y = point.x, point.y
            rmap[x] += 1
            cmap[y] += 1
        if rmap: ret = max(ret, max(rmap.values()))
        if cmap: ret = max(ret, max(cmap.values()))
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxPoints([Point()]))