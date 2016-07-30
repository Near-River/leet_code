#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Tags: Stack & String
        # ret, stack = True, []
        # lst1, lst2 = ['(', '[', '{'], [')', ']', '}']
        # for ch in s:
        #     if ch in lst1:
        #         stack.append(ch)
        #     elif ch in lst2:
        #         if stack == []: return False
        #         ch2 = stack.pop()
        #         if ch == ')' and ch2 != '(': return False
        #         if ch == ']' and ch2 != '[': return False
        #         if ch == '}' and ch2 != '{': return False
        #     else:
        #         return False
        # return stack == []

        """
        ASCII:
            ( ) : 40 41
            [ ] : 91 93
            { } : 123 125
        """
        ret, stack = True, []
        lst = ['(', '[', '{']
        for ch in s:
            if ch in lst:
                stack.append(ch)
            else:
                try:
                    ch2 = stack.pop()
                except IndexError:
                    return False
                if ord(ch) - ord(ch2) not in [1, 2]: return False

        return stack == []


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('('))
    print(solution.isValid('}'))
    print(solution.isValid('([)]'))
    print(solution.isValid('()[]{}'))
    print(ord('('), ord(')'))
    print(ord('['), ord(']'))
    print(ord('{'), ord('}'))
