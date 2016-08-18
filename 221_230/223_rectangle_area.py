#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
Assume that the total area is never beyond the maximum possible value of int.
"""


class Solution(object):
    def computeArea(self, x1, y1, x2, y2, x3, y3, x4, y4):
        overlap = 0
        if x3 < x2 and x4 > x1 and y3 < y2 and y4 > y1:
            width = min(x2, x4) - max(x1, x3)
            heigth = min(y2, y4) - max(y1, y3)
            overlap = width * heigth
        return (x2 - x1) * (y2 - y1) + (x4 - x3) * (y4 - y3) - overlap


if __name__ == '__main__':
    solution = Solution()
    print(solution.computeArea(0, 0, 0, 0, -1, -1, 1, 1))
