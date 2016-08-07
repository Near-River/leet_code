#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
The function prototype should be: bool isMatch(const char *s, const char *p)

Some examples:
    isMatch("aa","a") → false
    isMatch("aa","aa") → true
    isMatch("aaa","aa") → false
    isMatch("aa", "a*") → true
    isMatch("aa", ".*") → true
    isMatch("ab", ".*") → true
    isMatch("aab", "c*a*b") → true
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # solution one: Time Limit Exceeded
        if p == '': return s == ''
        if s == '':
            if len(p) >= 2 and p[1] == '*': return self.isMatch('', p[2:])
            return p == ''
        if len(s) == 1:
            if len(p) == 1: return False if p != '.' and p != s else True
            if len(p) >= 2:
                if p[1] == '*':
                    return self.isMatch(s, p[2:]) or self.isMatch('', p[2:])
                else:
                    if s != p[0] and p[0] != '.': return False
                    return self.isMatch('', p[1:])
        if len(s) > 1 and len(p) > 1:
            if p[0] != '*' and p[1] != '*':
                if s[0] != p[0] and p[0] != '.': return False
                return self.isMatch(s[1:], p[1:])
            elif p[1] == '*':
                i = 0
                if p[0] == '.':
                    if self.isMatch(s, p[2:]): return True
                    while i < len(s):
                        if self.isMatch(s[i + 1:], p[2:]): return True
                        i += 1
                    return False
                else:
                    if s[0] != p[0]: return self.isMatch(s, p[2:])
                    if self.isMatch(s, p[2:]): return True
                    while i < len(s) and s[i] == p[0]:
                        if self.isMatch(s[i + 1:], p[2:]): return True
                        i += 1
                    return False
        # return False

        # solution two: Dynamic Programming
        """
        dp[i][j]表示s[0:i-1]是否能和p[0:j-1]匹配。
        递推公式：由于只有p中会含有regular expression，所以以p[j-1]来进行分类。
        p[j-1] != '.' && p[j-1] != '*'：dp[i][j] = dp[i-1][j-1] && (s[i-1] == p[j-1])
        p[j-1] == '.'：dp[i][j] = dp[i-1][j-1]

        而关键的难点在于 p[j-1] = '*'。由于星号可以匹配0个或多个p[j-2]。
        1. 匹配0个元素，即消去p[j-2]，此时p[0: j-1] = p[0: j-3]
            dp[i][j] = dp[i][j-2]
        2. 匹配1个元素，此时p[0: j-1] = p[0: j-2]
            dp[i][j] = dp[i][j-1]
        3. 匹配多个元素，此时p[0: j-1] = { p[0: j-2], p[j-2], ... , p[j-2] }
            dp[i][j] = dp[i-1][j] && (p[j-2]=='.' || s[i-1]==p[j-2])
        """
        m, n = len(s), len(p)
        dp = [[False for i in range(n + 1)] for j in range(m + 1)]
        dp[0][0] = True  # means '' isMatch ''
        i = 1
        while i < n:  # pretreatment
            if p[i] != '*': break
            dp[0][i + 1] = True
            i += 2
        for i in range(m):
            for j in range(n):
                if p[j] != '.' and p[j] != '*':
                    dp[i + 1][j + 1] = dp[i][j] & (s[i] == p[j])
                elif p[j] == '.':
                    dp[i + 1][j + 1] = dp[i][j]
                else:  # p[j] == '*'
                    # no eliminate
                    flag1 = dp[i + 1][j - 1]
                    # eliminate an element
                    flag2 = dp[i + 1][j]
                    # eliminate more elements
                    flag3 = dp[i][j + 1] & (p[j - 1] == '.' or s[i] == p[j - 1])
                    dp[i + 1][j + 1] = flag1 or flag2 or flag3

        return dp[m][n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch("aa", "a"))
    print(solution.isMatch("aa", "aa"))
    print(solution.isMatch("aaa", "aa"))
    print(solution.isMatch("aa", "a*"))
    print(solution.isMatch("aa", ".*"))
    print(solution.isMatch("ab", ".*"))
    print(solution.isMatch("aab", "c*a*b"))
    print(solution.isMatch("ab", "ac*b"))
    print(solution.isMatch("", "c*a*b*"))
    print(solution.isMatch("aaa", "ab*ac*a"))
    print(solution.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
