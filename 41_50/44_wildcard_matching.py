#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be: bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # solution one: Time Limit Exceeded
        m, n = len(s), len(p)
        # if m > 300 and p[0] == p[-1] == '*': return False  # solve the TLE problem
        dp = [[False for i in range(n + 1)] for j in range(m + 1)]
        dp[0][0] = True  # means '' isMatch ''
        i = 0
        while i < n:  # pretreatment
            if p[i] != '*': break
            dp[0][i + 1] = True
            i += 1
        for i in range(m):
            for j in range(n):
                if p[j] != '?' and p[j] != '*':
                    dp[i + 1][j + 1] = dp[i][j] & (s[i] == p[j])
                elif p[j] == '?':
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    # Match empty sequence or more of any character
                    dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1]

        # return dp[m][n]

        # solution two
        m, n = len(s), len(p)
        i, j = 0, 0
        star, preS = -1, -1
        while i < m:
            if j < n and p[j] != '*' and (p[j] == '?' or s[i] == p[j]):
                j += 1
                i += 1
            elif j < n and p[j] == '*':
                preS = i
                star = j
                j = star + 1
            elif star != -1:
                preS += 1  # reset the index of i and j, recover from the last failed matching.
                i = preS
                j = star + 1
            else:
                return False
        while j < n:  # 处理p结尾处多余的*号
            if p[j] != '*': return False
            j += 1
        return j >= n


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch("aa", "**aa*"))
    print(solution.isMatch("aa", "a**"))
    print(solution.isMatch("ab", "?*"))
    print(solution.isMatch("aab", "c*a*b"))
    print(solution.isMatch("ab", "ac*b"))
    print(solution.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
    print(solution.isMatch("abefcdgiescdfimde", "ab*cd?i*de"))
