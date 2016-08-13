#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Related to question Excel Sheet Column Title
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        base = 1
        for i in range(len(s) - 1, -1, -1):
            ret += base * (ord(s[i]) - ord('A') + 1)
            base *= 26
        return ret


if __name__ == '__main__':
    solution = Solution()
