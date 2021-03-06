#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.

罗马数字规则：
1， 罗马数字共有7个，即I（1）、V（5）、X（10）、L（50）、C（100）、D（500）和M（1000）
2， 重复次数：一个罗马数字最多重复3次
3， 右加左减：
    在较大的罗马数字的右边记上较小的罗马数字，表示大数字加小数字
    在较大的罗马数字的左边记上较小的罗马数字，表示大数字减小数字
4， 左减的数字有限制，仅限于I、X、C，且放在大数的左边只能用一个
    左减数字必须为一位，比如8写成VIII，而非IIX
    左减时不可跨越一个位数。比如，99不可以用IC（100 - 1）表示，而是用XCIX（[100 - 10] + [10 - 1]）表示
    V 和 X 左边的小数字只能用Ⅰ
    L 和 C 左边的小数字只能用X
    D 和 M 左边的小数字只能用C
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ['', 'M', 'MM', 'MMM']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]


if __name__ == '__main__':
    solution = Solution()
    print(solution.intToRoman(1234))