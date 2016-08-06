#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
The number of ways decoding "12" is 2.
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0: return 0
        dp = [0 for i in range(length)]
        dp.append(1)
        i = length - 2
        if s[-1] != '0': dp[length - 1] = 1
        while i >= 0:
            if s[i] != '0':
                n = int(s[i:i + 2])
                if 10 <= n <= 26:
                    dp[i] = dp[i + 1] + dp[i + 2]
                else:
                    dp[i] = dp[i + 1]
            i -= 1

        return dp[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numDecodings('0'))
    print(solution.numDecodings('12'))
