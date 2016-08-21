#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
Below is one possible representation of s1 = "great":
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".
Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".
Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
"""


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # solution one
        if s1 == s2: return True
        lst1, lst2 = list(s1), list(s2)  # optimization - 1
        lst1.sort()
        lst2.sort()
        if lst1 != lst2: return False

        # _sum1 = _sum2 = 0  # optimization - 2
        # for i in range(len(s1)):
        #     _sum1 += ord(s1[i])
        #     _sum2 += ord(s2[i])
        # if _sum1 != _sum2: return False

        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]): return True
            if self.isScramble(s1[len(s1) - i:], s2[:i]) and self.isScramble(s1[:len(s1) - i], s2[i:]): return True
        # return False

        # solution two: Dynamic Programming
        """
        res[i][j][len]表示的是以i和j分别为s1和s2起点的长度为len的字符串是不是互为scramble
        """
        if s1 == '': return True
        n = len(s1)
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = s1[i] == s2[j]
        for _len in range(2, n + 1):
            for i in range(n - _len + 1):
                for j in range(n - _len + 1):
                    for k in range(1, _len):
                        if dp[i][j][k] and dp[i + k][j + k][_len - k] or dp[i][j + _len - k][k] and dp[i + k][j][_len - k]:
                            dp[i][j][_len] = True
                            break

        return dp[0][0][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isScramble('great', 'rgtae'))
    print(solution.isScramble('great', 'rateg'))
