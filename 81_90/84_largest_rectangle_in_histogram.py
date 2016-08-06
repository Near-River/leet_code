#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.

For example,
Given heights = [2,1,5,6,2,3], return 10.
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # slution one: Time Limit Exceeded
        # length = len(heights)
        # ret = 0
        # for i in range(length):
        #     if i > 0 and heights[i] <= heights[i-1]: continue
        #     minHeight = heights[i]
        #     for j in range(i, length):
        #         minHeight = min(minHeight, heights[j])
        #         ret = max(ret, (j - i + 1) * minHeight)
        # return ret

        # solution two: Time Limit Exceeded
        length = len(heights)
        ret = 0
        for i in range(length):
            start = end = i
            height = heights[i]
            while start - 1 >= 0 and heights[start - 1] >= height:
                start -= 1
            while end + 1 < length and heights[end + 1] >= height:
                end += 1
            ret = max(ret, (end - start + 1) * height)
        # return ret

        # solution three
        ret, stack = 0, []
        heights.append(0)
        length = len(heights)
        i = 0
        while i < length:
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                idx = stack.pop()
                rn = i
                ln = stack[-1] if stack else -1
                ret = max(ret, (rn - ln - 1) * heights[idx])

        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestRectangleArea(heights=[2, 1, 2]))
    print(solution.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]))
    print(solution.largestRectangleArea(heights=[4, 2, 0, 3, 2, 5]))
