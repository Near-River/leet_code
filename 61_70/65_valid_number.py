#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
"""


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        0 初始无输入或者只有space的状态
        1 输入了数字之后的状态
        2 前面无数字，只输入了Dot的状态
        3 输入了符号之后的状态
        4 前面有数字和有dot的状态
        5 'e' or 'E'输入后的状态
        6 输入e之后输入Sign的状态
        7 输入e后输入数字的状态
        8 前面有有效数输入之后，输入space的状态

        可结束状态：1, 4, 7, 8
        """
        INVALID, SPACE, SIGN, DIGIT, DOT, EXPONENT = (i for i in range(6))
        state = 0
        transitionTable = [
            [-1, 0, 3, 1, 2, -1],
            [-1, 8, -1, 1, 4, 5],
            [-1, -1, -1, 4, -1, -1],
            [-1, -1, -1, 1, 2, -1],
            [-1, 8, -1, 4, -1, 5],
            [-1, -1, 6, 7, -1, -1],
            [-1, -1, -1, 7, -1, -1],
            [-1, 8, -1, 7, -1, -1],
            [-1, 8, -1, -1, -1, -1]
        ]
        for ch in s:
            if ch.isdigit():
                _input = DIGIT
            elif ch == '+' or ch == '-':
                _input = SIGN
            elif ch == '.':
                _input = DOT
            elif ch.lower() == 'e':
                _input = EXPONENT
            elif ch == ' ':
                _input = SPACE
            else:
                _input = INVALID
            state = transitionTable[state][_input]
            if state == -1: return False
        return True if state in (1, 4, 7, 8) else False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isNumber(' 0.1 '))
    print(solution.isNumber('1 a'))
    print(solution.isNumber('2e10'))
    print(solution.isNumber('-3.e+3'))
