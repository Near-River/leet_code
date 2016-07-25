#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        if x == 0:
            return x
        if x < 0:
            flag = True
            x *= -1
        s = str(x)
        while True:
            if s.endswith('0'):
                s = s[:-1]
            else:
                break
        # print(''.join(list(reversed(s))))
        s = s[::-1]
        x = -1 * int(s) if flag else int(s)

        # returns 0 when the reversed integer overflows
        if x > 2 ** 31 - 1 or x < -1 * (2 ** 31):
            return 0

        return x


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(2**31))
    print(solution.reverse(12000))
    print(solution.reverse(-1234))
