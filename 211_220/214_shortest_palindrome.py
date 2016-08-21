#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the
shortest palindrome you can find by performing this transformation.

For example:
Given "aacecaaa", return "aaacecaaa".
Given "abcd", return "dcbabcd".
"""


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # solution one: Time Limit Exceeded
        # def isPalindrome(s, start, end):
        #     while start < end:
        #         if s[start] != s[end]: return False
        #         start += 1
        #         end -= 1
        #     return True
        #
        # if s == '': return ''
        # n = len(s)
        # i = _len = (n - 1) // 2
        # while i >= 0:
        #     end = n - 2 * (_len - i) - 1
        #     if isPalindrome(s, 0, end): return (s[end + 1:])[::-1] + s
        #     if isPalindrome(s, 0, end - 1): return (s[end:])[::-1] + s
        #     i -= 1

        # solution two - 1: KMP
        r = s[::-1]
        t = s + '#' + r + '#'
        _next = [0] * len(t)
        _next[0] = -1
        i, k = 0, -1
        while i < len(t) - 1:
            if k == -1 or t[i] == t[k]:
                k += 1
                i += 1
                _next[i] = k
            else:
                k = _next[k]
        # return r[:len(s) - _next[-1]] + s

        # solution two - 2
        r = s[::-1]
        t = s + '#' + r
        _next = [0] * len(t)
        for i in range(1, len(t)):
            k = _next[i - 1]
            while k > 0 and t[i] != t[k]: k = _next[k - 1]
            if t[i] == t[k]: k += 1
            _next[i] = k

        return r[:len(s) - _next[-1]] + s


if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestPalindrome("aacecaaa"))
    print(solution.shortestPalindrome("aaaaa"))
