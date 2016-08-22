#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""


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
        n = len(points)
        if n <= 2: return n
        ret, map = 0, {}
        for i in range(n - 1):
            p1 = points[i]
            infinite = duplicate = 1
            map.clear()
            for j in range(i + 1, n):
                p2 = points[j]
                dx, dy = p2.x - p1.x, p2.y - p1.y
                if dx == 0:
                    if dy == 0: duplicate += 1
                    infinite += 1
                else:
                    k = float(dy) / dx
                    if k not in map:
                        map[k] = 1
                    else:
                        map[k] += 1
            _max = 0 if not map else max(list(map.values()))
            ret = max(ret, duplicate + _max, infinite)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxPoints([Point(1, 1), Point(1, 1), Point(2, 3)]))
    print(solution.maxPoints([Point(3, 10), Point(0, 2), Point(0, 2), Point(3, 10)]))
    print(solution.maxPoints([Point(0, 0), Point(1, 1), Point(1, -1)]))
    print(solution.maxPoints(
        [Point(84, 250), Point(0, 0), Point(1, 0), Point(0, -70), Point(0, -70), Point(1, -1), Point(21, 10),
         Point(42, 90), Point(-42, -230)]))
