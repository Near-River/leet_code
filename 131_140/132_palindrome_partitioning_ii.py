#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        def isPalindrome(s):
            length = len(s)
            if length < 2: return True
            i, j = 0, length - 1
            while i < j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True

        # solution one
        # length = len(s)
        # if length < 2: return 0
        # dp = [[0] * length for i in range(length)]
        #
        # for count in range(1, length):
        #     for i in range(length - count):
        #         j = i + count
        #         part = s[i:j + 1]
        #         if isPalindrome(part):
        #             dp[i][j] = 0
        #         else:
        #             _minCut = 2147483647
        #             for k in range(1, j - i + 1):
        #                 _minCut = min(_minCut, dp[i][i + k - 1] + dp[i + k][j] + 1)
        #             dp[i][j] = _minCut
        # return dp[0][-1]

        # optimization
        """
        dp[i,n] = min(dp[i, j] + dp[j+1,n] + 1)  i <= j <n
        简化dp[i][j]为dp[i]，表示从0到i的minCut.
        dp[i]=min(dp[k]+1,      dp[k]+i-k), 0<=k<i.
        (s[k+1, i]是回文串）    (s[k+1, i]不是回文串)

        定义函数 P[i][j] = true if [i,j]为回文
        那么 P[i][j] = str[i] == str[j] && P[i+1][j-1];
        """
        length = len(s)
        if length < 2: return 0
        dp = [i for i in range(length)]
        palindrome = [[False for i in range(length)] for j in range(length)]
        for i in range(length): palindrome[i][i] = True
        for i in range(1, length):
            if (i <= 1 or palindrome[1][i - 1]) and s[0] == s[i]:
                dp[i] = 0
                palindrome[0][i] = True
            for j in range(i):
                if (i <= j + 2 or palindrome[j + 2][i - 1]) and s[j + 1] == s[i]:
                    palindrome[j + 1][i] = True
                    dp[i] = min(dp[i], dp[j] + 1)
                else:
                    dp[i] = min(dp[i], dp[j] + i - j)
        # return dp[-1]

        # solution two
        dp = [length - i for i in range(length + 1)]
        palindrome = [[False for i in range(length)] for j in range(length)]
        for i in range(length - 1, -1, -1):
            for j in range(i, length):
                if s[j] == s[i] and (j - i < 2 or palindrome[i + 1][j - 1]):
                    palindrome[i][j] = True
                    dp[i] = min(dp[i], dp[j + 1] + 1)

        return dp[0] - 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCut('aab'))
    print(solution.minCut('aabbc'))
    print(solution.minCut('aabbcd'))
    print(solution.minCut(
        "kwtbjmsjvbrwriqwxadwnufplszhqccayvdhhvscxjaqsrmrrqngmuvxnugdzjfxeihogzsdjtvdmkudckjoggltcuybddbjoizu"))
