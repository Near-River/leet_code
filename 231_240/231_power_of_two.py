#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an integer, write a function to determine if it is a power of two.
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        while n > 0:
            if n & 1 == 1: count += 1
            n >>= 1
        return count == 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfTwo(1))
    print(solution.isPowerOfTwo(2))
    print(solution.isPowerOfTwo(9))
    print(solution.isPowerOfTwo(1 << 21))
