#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"
Return 3.
"""


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # m, n = len(s), len(t)
        # if m < n: return 0
        # dp = [[0] * (n + 1) for i in range(m + 1)]
        # for i in range(1 + m): dp[i][0] = 1
        # for c in range(1, 1 + n):
        #     for r in range(c, 1 + m):
        #         if c == r:
        #             if dp[r - 1][c - 1] and s[r - 1] == t[c - 1]: dp[r][c] = 1
        #         else:
        #             if s[r - 1] == t[c - 1]:
        #                 dp[r][c] = dp[r - 1][c - 1] + dp[r - 1][c]
        #             else:
        #                 dp[r][c] = dp[r - 1][c]
        #
        # return dp[-1][-1]

        # optimization
        m, n = len(s), len(t)
        if m < n: return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        for r in range(1, m + 1):
            for c in range(n, 0, -1):
                if s[r - 1] == t[c - 1]: dp[c] += dp[c - 1]

        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numDistinct('rabbbit', 'rabbit'))
