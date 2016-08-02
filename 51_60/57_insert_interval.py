#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return 'Interval: (%d, %d)' % (self.start, self.end)


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        length, i = len(intervals), 0
        while i < length:
            if intervals[i].start >= newInterval.start: break
            i += 1
        # merge the overlapping interval if exist
        start = end = i
        if i - 1 >= 0 and intervals[i - 1].end >= newInterval.start: start = i - 1
        if i - 1 >= 0 and intervals[i - 1].end >= newInterval.end: end = i - 1
        while i < len(intervals):
            if intervals[i].start > newInterval.end:
                end = i - 1
                break
            end, i = i, i + 1
        ret = intervals[:start]
        s, e = newInterval.start, newInterval.end
        if 0 <= start < length and intervals[start].start < s: s = intervals[start].start
        if 0 <= end < length and intervals[end].end > e: e = intervals[end].end
        ret.append(Interval(s, e))
        ret.extend(intervals[end + 1:])

        return ret


if __name__ == '__main__':
    solution = Solution()
    intervals = [Interval(1, 3), Interval(6, 9)]
    intervals2 = [Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)]
    print(solution.insert(intervals, Interval(2, 5)))
    print(solution.insert(intervals2, Interval(4, 9)))
    # print(solution.insert([], Interval(5, 7)))
    # print(solution.insert([Interval(1, 5)], Interval(2, 3)))
    # print(solution.insert([Interval(2, 5)], Interval(1, 6)))
    # print(solution.insert([Interval(1, 5)], Interval(2, 8)))
    # print(solution.insert([Interval(3, 5)], Interval(1, 2)))
    # print(solution.insert([Interval(3, 5)], Interval(7, 9)))
