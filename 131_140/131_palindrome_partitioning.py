#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.
For example, given s = "aab",
Return
[
    ["aa", "b"],
    ["a", "a", "b"]
]
"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
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

        def builder(s):
            if s == '': return []
            if len(s) == 1: return [[s]]
            ret = []
            for i in range(len(s)):
                part = s[:i + 1]
                if isPalindrome(part):
                    _ret = builder(s[i + 1:])
                    if _ret:
                        for lst in _ret: ret.append([part] + lst)
                    else:
                        ret.append([s])
            return ret

        return builder(s)


if __name__ == '__main__':
    solution = Solution()
    print(solution.partition('aab'))
    print(solution.partition('abba'))
