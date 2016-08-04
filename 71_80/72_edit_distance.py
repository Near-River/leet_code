#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:
    a) Insert a character
    b) Delete a character
    c) Replace a character
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        """
        动态数组dp[word1.length+1][word2.length+1]
        dp[i][j]表示从word1前i个字符转换到word2前j个字符最少的步骤数。
        假设word1现在遍历到字符x，word2遍历到字符y（word1当前遍历到的长度为i，word2为j）。
        以下两种可能性：
        1. x==y，那么不用做任何编辑操作，所以dp[i][j] = dp[i-1][j-1]
        2. x != y
           (1) 在word1插入y， 那么dp[i][j] = dp[i][j-1] + 1
           (2) 在word1删除x， 那么dp[i][j] = dp[i-1][j] + 1
           (3) 把word1中的x用y来替换，那么dp[i][j] = dp[i-1][j-1] + 1
           最少的步骤就是取这三个中的最小值。
        最后返回 dp[word1.length+1][word2.length+1] 即可。
        """
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for i in range(len1 + 1)]
        for i in range(len1 + 1): dp[i][0] = i
        for j in range(len2 + 1): dp[0][j] = j
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[len1][len2]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance('word', 'world'))
    print(solution.minDistance('wardly', 'world'))
