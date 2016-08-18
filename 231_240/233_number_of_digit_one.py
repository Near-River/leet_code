#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

Hint: Beware of overflow.
"""


class Solution(object):
    def digitCount(self, n):
        if n == 0:
            return 0
        else:
            return 10 ** (n - 1) + 10 * self.digitCount(n - 1)

    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10: return 0 if n <= 0 else 1
        digit = 0
        count, base = 1, 1
        while n // base >= 10:
            base *= 10
            count += 1

        a = n // base
        digit += a * self.digitCount(count - 1)
        digit += (n % base + 1) if a == 1 else 10 ** (count - 1)
        digit += self.countDigitOne(n % base)
        return digit


if __name__ == '__main__':
    solution = Solution()
    print(solution.countDigitOne(13))
    print(solution.countDigitOne(32))
