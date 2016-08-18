#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division
should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operStack, numsStack = [], []
        operator = ['*', '/', '+', '-']
        i = len(s) - 1
        while i >= 0:
            ch = s[i]
            i -= 1
            if ch == ' ': continue
            if ch in operator:
                operStack.append(ch)
            else:
                j = i
                while j >= 0 and '0' <= s[j] <= '9': j -= 1
                numsStack.append(int(s[j + 1:i + 2]))
                i = j

        def calculate(opers, nums):
            while opers:
                oper = opers.pop()
                num1 = nums.pop()
                num2 = nums.pop()
                if oper == '*':
                    nums.append(num1 * num2)
                elif oper == '/':
                    nums.append(num1 // num2)
            return nums[0]

        i = len(operStack) - 1
        while i >= 0:  # do multiplication or division calculation
            if operStack[i] in ('*', '/'):
                j = i - 1
                while j >= 0 and operStack[j] in ('*', '/'): j -= 1
                res = calculate(operStack[j + 1:i + 1], numsStack[j + 1:i + 2])
                operStack = operStack[:j + 1] + operStack[i + 1:]
                numsStack = numsStack[:j + 1] + [res] + numsStack[i + 2:]
                i = j
            else:
                i -= 1

        while operStack:  # do addition or subtraction calculation
            oper = operStack.pop()
            num1 = numsStack.pop()
            num2 = numsStack.pop()
            if oper == '+':
                numsStack.append(num1 + num2)
            elif oper == '-':
                numsStack.append(num1 - num2)
        return numsStack[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.calculate("1+2*3/4+3-4*5"))
