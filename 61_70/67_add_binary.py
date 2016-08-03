#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = a[::-1], b[::-1]
        len1, len2 = len(a), len(b)
        ret, i, carry = '', 0, 0
        while i < max(len1, len2):
            m = 0 if i >= len1 else int(a[i])
            n = 0 if i >= len2 else int(b[i])
            temp = m + n + carry
            carry = temp // 2
            ret += str(temp % 2)
            i += 1
        if carry: ret += '1'
        return ret[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary('0', '0'))
    print(solution.addBinary('11', '1'))
    print(solution.addBinary('1010', '1011'))
