#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        numStack = []

        for s in tokens:
            if s.isdigit() or len(s) > 1:
                numStack.append(int(s))
            else:
                num1, num2, res = 0, 0, 0
                if numStack: num2 = numStack.pop()
                if numStack: num1 = numStack.pop()
                if s == '+':
                    res = num1 + num2
                elif s == '-':
                    res = num1 - num2
                elif s == '*':
                    res = num1 * num2
                elif s == '/':
                    # res = int(num1 / num2)
                    res = -((-num1) // num2) if num1 * num2 < 0 else num1 // num2
                numStack.append(res)
        return numStack[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.evalRPN(["2", "1", "+", "3", "*"]))
    print(solution.evalRPN(["4", "13", "5", "/", "+"]))
    print(solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
