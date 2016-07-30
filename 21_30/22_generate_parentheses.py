#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]

Catalan:
    h(n)= h(0)*h(n-1)+h(1)*h(n-2) + ... + h(n-1)h(0) (n>=2)
     1, 1, 2, 5, 14, 42, 132, 429, 1430, ...
"""

from copy import copy


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        # solution one - 1
        def find_parenthesis(n):
            if n == 1: return {'()'}
            ret = set()
            parenthesis = find_parenthesis(n - 1)
            for p in parenthesis:
                p = list(p)
                curr, next = 0, 1
                while curr < len(p):
                    _p = copy(p)
                    _p.insert(curr, '()')
                    ret.add(''.join(_p))
                    if p[curr] != '(' or next >= len(p):
                        curr += 1
                        next = curr + 1
                    else:
                        if p[next] == ')':
                            _p = copy(p)
                            _p.insert(next, ')')
                            _p.insert(curr, '(')
                            ret.add(''.join(_p))
                        next += 1
            return ret

        # return list(find_parenthesis(n))

        # solution one - 2
        # def find_parenthesis(n):
        #     if n == 1: return {'()'}
        #     ret = set()
        #     parenthesis = find_parenthesis(n - 1)
        #     for p in parenthesis:
        #         curr, prev = 0, -1
        #         for curr in range(len(p)):
        #             p = list(p)
        #             _p = copy(p)
        #             _p.insert(curr, '()')
        #             ret.add(''.join(_p))
        #             if prev != -1 and p[curr] == p[prev]: continue
        #             next = curr + 1
        #             while next < len(p):
        #                 if p[next] == ')':
        #                     _p = copy(p)
        #                     _p.insert(next, ')')
        #                     _p.insert(curr, '(')
        #                     ret.add(''.join(_p))
        #                 next += 1
        #             if p[curr] == '(': prev = curr
        #     return ret
        #
        # return list(find_parenthesis(n))

        # solution three
        """
        Rules:
            针对一个长度为2n的合法排列，第1到2n个位置都满足如下规则：左括号的个数大于等于右括号的个数。
            打印括号：假设在位置k我们还剩余left个左括号和right个右括号，如果left>0，则可以直接打印左括号，而不违背规则。
                能否打印右括号，还必须验证left和right的值是否满足规则，如果left>=right，则不能打印右括号，因为打印
                会违背合法排列的规则。如果left和right均为零，则说明已经完成一个合法排列，可将其打印出来。
        """
        ret = []

        def find_all_parenthesis(left, right, result):
            if left == 0 and right == 0:
                ret.append(result)
            if left > 0:
                find_all_parenthesis(left - 1, right, result + '(')
            if left < right:
                find_all_parenthesis(left, right - 1, result + ')')

        find_all_parenthesis(left=n, right=n, result='')
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))
    print(solution.generateParenthesis(4))
