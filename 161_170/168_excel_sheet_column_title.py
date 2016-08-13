#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = ''
        while n >= 26:
            mod = n % 26
            if mod != 0:
                ret += chr(64 + mod)
            else:
                ret += chr(90)
                n -= 1
            n //= 26
        if n != 0: ret += chr(64 + n)
        return ret[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.convertToTitle(5))
    print(solution.convertToTitle(26))
    print(solution.convertToTitle(2 * 26))
    print(solution.convertToTitle(2 * 26 * 26))
    print(solution.convertToTitle(1 * 26 * 26 + 2 * 26 + 3))
