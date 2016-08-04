#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        # solution one
        def search_sqrt(x, down, up):
            if down ** 2 > x:
                return search_sqrt(x, down // 2, down)
            elif down ** 2 < x:
                if (down + 1) ** 2 > x: return down
                return search_sqrt(x, down + 1, (down + up) // 2)
            return down

        # return search_sqrt(x, x // 2, x)

        down = 0
        while True:
            base = 1
            while (down + base) ** 2 <= x: base <<= 1
            down += base >> 1
            if down ** 2 <= x < (down + 1) ** 2: return down


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(1))
    print(solution.mySqrt(9))
    print(solution.mySqrt(17))
    print(solution.mySqrt(201))
    print(solution.mySqrt(2147395599))
