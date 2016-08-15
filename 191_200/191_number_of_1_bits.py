#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # solution one
        count = 0
        temp = 1
        for i in range(32):
            if n & temp != 0: count += 1
            temp <<= 1
        # return count

        # solution two
        count = 0
        for i in range(32):
            if n & 1 == 1: count += 1
            n >>= 1
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingWeight(11))
