#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one
or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        # solution one: Time Limit Exceeded
        if len(s) < 1: return False
        for i in range(len(s) - 1):
            w = s[:i + 1]
            if w not in wordDict: continue
            if self.wordBreak(s[i + 1:], wordDict): return True
        if s in wordDict: return True
        # return False

        # solution two: Dynamic Programming
        length = len(s)
        dp = [False] * length
        for i in range(length):
            if s[:i + 1] in wordDict:
                dp[i] = True
                continue
            for j in range(i):
                if dp[j] and s[j + 1:i+1] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordBreak('leetcode', ['leet', 'code']))
