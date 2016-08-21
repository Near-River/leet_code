#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
it is able to trap after raining.

For example, Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ret = 0
        stack = []
        for h in height:
            if stack and stack[0] <= h:
                _h = stack[0]
                while stack: ret += (_h - stack.pop())
            stack.append(h)
        while len(stack) > 1:
            _h = stack.pop()
            if stack[-1] < _h:
                while stack and stack[-1] < _h:
                    ret += (_h - stack.pop())

        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
