#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if s1 == '': return s2 == s3
        if s2 == '': return s1 == s3
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n3 != n1 + n2: return False
        dp = [set(), set()]
        if s3[0] == s1[0]: dp[0].add((1, 0))
        if s3[0] == s2[0]: dp[0].add((0, 1))
        if not dp[0]: return False
        prev, curr = 1, 0
        for i in range(1, n3):
            prev, curr = curr, prev
            dp[curr].clear()
            for j in dp[prev]:
                e1, e2 = j
                if e1 < n1 and s3[i] == s1[e1]: dp[curr].add((e1 + 1, e2))
                if e2 < n2 and s3[i] == s2[e2]: dp[curr].add((e1, e2 + 1))
            if not dp[curr]: return False
        return True


if __name__ == '__main__':
    solution = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    print(solution.isInterleave(s1, s2, 'aadbbcbcac'))
    print(solution.isInterleave(s1, s2, 'aadbbbaccc'))
