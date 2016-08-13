#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n >= 5:
            ret += n // 5
            n //= 5
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.trailingZeroes(128))
