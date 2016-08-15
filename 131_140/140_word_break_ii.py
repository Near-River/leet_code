#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """

        # solution one
        # length = len(s)
        # dp = [[] for i in range(length)]
        # for i in range(length):
        #     w = s[:i + 1]
        #     if w in wordDict:
        #         dp[i].append(w)
        #     for j in range(i):
        #         if dp[j] and s[j + 1:i + 1] in wordDict:
        #             for _s in dp[j]: dp[i].append(_s + ' ' + s[j + 1:i + 1])
        # return dp[-1]

        # solution two: Dynamic Programming + DFS
        length = len(s)
        possible = [False] * length
        for i in range(length):
            if s[:i + 1] in wordDict:
                possible[i] = True
                continue
            for j in range(i):
                if possible[j] and s[j + 1:i + 1] in wordDict:
                    possible[i] = True
                    break

        def helper(s, end):
            ret = []
            for i in range(end):
                if possible[i] and s[i + 1:end + 1] in wordDict:
                    for w in helper(s, i): ret.append(w + ' ' + s[i + 1:end + 1])
            if s[:end + 1] in wordDict: ret.append(s[:end + 1])
            return ret

        return helper(s, length - 1) if possible[-1] else []


if __name__ == '__main__':
    solution = Solution()
    s = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    print(solution.wordBreak(s, dict))
    s2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    dict2 = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    print(solution.wordBreak(s2, dict2))
