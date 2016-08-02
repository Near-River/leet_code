#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3], [2,6], [8,10], [15,18],
return [1,6], [8,10], [15,18].
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return 'Interval: (%d, %d)' % (self.start, self.end)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return []
        intervals = sorted(intervals, key=lambda i: i.start)
        ret, length = [], len(intervals)
        for i in range(length - 1):
            i1, i2 = intervals[i], intervals[i + 1]
            if i2.start > i1.end:
                ret.append(i1)
            else:
                i2.start, i2.end = i1.start, max(i1.end, i2.end)
        ret.append(intervals[-1])
        return ret


if __name__ == '__main__':
    solution = Solution()
    intervals = [Interval(1, 3), Interval(15, 18), Interval(2, 6), Interval(8, 10)]
    intervals2 = [Interval(1, 4), Interval(0, 2), Interval(3, 5)]
    print(solution.merge(intervals))
    print(solution.merge(intervals2))
