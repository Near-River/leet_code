#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operStack, numsStack = [], []
        operator = ['(', ')', '+', '-']
        i = len(s) - 1
        while i >= 0:
            ch = s[i]
            i -= 1
            if ch == ' ': continue
            if ch in operator:
                if ch == '(':
                    if operStack[-1] == ')':
                        operStack.pop()
                    elif len(numsStack) >= 2:
                        while operStack[-1] != ')':
                            oper = operStack.pop()
                            num1 = numsStack.pop()
                            num2 = numsStack.pop()
                            if oper == '+':
                                numsStack.append(num1 + num2)
                            elif oper == '-':
                                numsStack.append(num1 - num2)
                        operStack.pop()
                else:
                    operStack.append(ch)
            else:
                j = i
                while j >= 0 and '0' <= s[j] <= '9': j -= 1
                numsStack.append(int(s[j + 1:i + 2]))
                i = j
        while operStack:
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
    print(solution.calculate("(7)-(0)+(4)"))
    print(solution.calculate("(1-(3-4))"))
    print(solution.calculate(" 2-1 + 2 "))
    print(solution.calculate("(11-(4-5+2)+3)-(6+8)"))
