#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number
by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or
it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number
    1**2 + 9**2 = 82
    8**2 + 2**2 = 68
    6**2 + 8**2 = 100
    1**2 + 0**2 + 0**2 = 1
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def squareSum(n):
            _sum = 0
            while n >= 10:
                _sum += (n % 10) ** 2
                n //= 10
            _sum += n ** 2
            return _sum

        hash = {n: True}
        while True:
            n = squareSum(n)
            if n == 1: return True
            if n in hash: return False
            hash[n] = True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(19))
