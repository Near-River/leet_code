#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # solution one: Time Limit Exceeded
        # def isValidParentheses(s):
        #     stack = []
        #     for ch in s:
        #         if ch == '(':
        #             stack.append('(')
        #         else:
        #             if not stack: return False
        #             stack.pop()
        #     return not stack
        #
        # ret = 0
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         j = len(s) - 1
        #         while i < j:
        #             if s[j] == ')':
        #                 if isValidParentheses(s[i:j + 1]): ret = max(ret, j - i + 1)
        #             j -= 1
        #     i += 1
        #
        # return ret

        # solution two: Dynamic Programming
        length = len(s)
        if length <= 1: return 0
        i = length - 2
        d = [0 for i in range(length)]
        while i >= 0:
            if s[i] == '(':
                idx = 2 * d[i + 1] + i + 1
                if idx < length and s[idx] == ')':
                    d[i] = d[i + 1] + 1
                    if idx + 1 < length and s[idx + 1] == '(': d[i] += d[idx + 1]
            i -= 1
        # return max(d) * 2

        # solution three: Stack
        stack = []
        start, ret = -1, 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if not stack:
                        ret = max(ret, i - start)
                    else:
                        ret = max(ret, i - stack[-1])
                else:
                    start = i

        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestValidParentheses(")("))
    print(solution.longestValidParentheses("(()"))
    print(solution.longestValidParentheses("()(()"))
    print(solution.longestValidParentheses("()(()(()("))
    print(solution.longestValidParentheses("()(()(((()))("))
    print(solution.longestValidParentheses(")()(()(((()))()("))
