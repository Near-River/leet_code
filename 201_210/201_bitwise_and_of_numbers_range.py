#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while n > m:
            n >>= 1
            m >>= 1
            i += 1

        return m << i


if __name__ == '__main__':
    solution = Solution()
    print(solution.rangeBitwiseAnd(5, 7))
    print(solution.rangeBitwiseAnd(5, 30))
