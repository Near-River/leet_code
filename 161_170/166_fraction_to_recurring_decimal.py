#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.

For example,
    Given numerator = 1, denominator = 2, return "0.5".
    Given numerator = 2, denominator = 1, return "2".
    Given numerator = 2, denominator = 3, return "0.(6)".

Hint:
    No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # negative or positive
        ret = '' if numerator * denominator >= 0 else '-'
        a, b = abs(numerator), abs(denominator)
        pos = 0
        if a >= b:
            pos = a // b
            a = a % b
        if a == 0: return ret + str(pos)
        a *= 10
        decimal = []
        map = {a // 10: 0}
        loop = False
        start = end = -1
        i = 1
        while True:
            div, mod = a // b, a % b
            decimal.append(str(div))
            if mod == 0: break
            if mod in map:
                loop = True
                start, end = map[mod], i
                break
            map[mod] = i
            a, i = mod * 10, i + 1
        ret += (str(pos) + '.')
        if loop:
            ret += (''.join(decimal[:start]) + '(' + ''.join(decimal[start:end]) + ')')
        else:
            ret += ''.join(decimal)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.fractionToDecimal(1, 2))
    print(solution.fractionToDecimal(2, 1))
    print(solution.fractionToDecimal(2, 3))
    print(solution.fractionToDecimal(2, 13))
    print(solution.fractionToDecimal(1, 432), 1 / 432)
    print(solution.fractionToDecimal(1, 99), 1 / 99)
