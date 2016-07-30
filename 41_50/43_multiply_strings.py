#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
    The numbers can be arbitrarily large and are non-negative.
    Converting the input string to integer is NOT allowed.
    You should NOT use internal library such as BigInteger.
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # solution one
        len1, len2 = len(num1), len(num2)
        num1, num2 = num1[::-1], num2[::-1]
        ret = []
        for i in range(len2):
            multiplier, carry = int(num2[i]), 0
            for j in range(len1):
                n = int(num1[j])
                left = (multiplier * n + carry) % 10
                carry = (multiplier * n + carry) // 10
                while i + j >= len(ret): ret.append('0')
                if i == 0:
                    ret[i + j] = str(left)
                else:
                    m = int(ret[i + j])
                    carry += (left + m) // 10
                    ret[i + j] = str((left + m) % 10)
            if carry > 0: ret.append(str(carry))
        ret = ''.join(ret)
        while ret.endswith('0') and len(ret) > 1: ret = ret[:-1]
        # return ret[::-1]

        # solution two
        len1, len2 = len(num1), len(num2)
        num1, num2 = num1[::-1], num2[::-1]
        d, ret = [], []
        for i in range(len1 + len2): d.append(0)
        for i in range(len1):
            for j in range(len2):
                d[i + j] += int(num1[i]) * int(num2[j])
        length = len(d)
        d.append(0)
        for i in range(length):
            mod = d[i] % 10
            carry = d[i] // 10
            d[i + 1] += carry
            ret.append(str(mod))
        ret = ret[::-1]
        while ret[0] == '0' and len(ret) > 1: ret.remove('0')
        return ''.join(ret)

        # solution three
        # return str(int(num1) * int(num2))


if __name__ == '__main__':
    solution = Solution()
    print(solution.multiply('0', '0'), 0 * 0)
    print(solution.multiply('123', '34'), 123 * 34)
    print(solution.multiply('567', '89'), 567 * 89)
    print(solution.multiply('999', '0'), 0)
