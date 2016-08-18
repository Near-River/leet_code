#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two
characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.
Given "foo", "bar", return false.
Given "paper", "title", return true.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == '': return t == ''
        map, map2 = {}, {}
        for i in range(len(s)):
            if s[i] not in map:
                map[s[i]] = t[i]
            elif t[i] != map[s[i]]:
                return False
            if t[i] not in map2:
                map2[t[i]] = s[i]
            elif s[i] != map2[t[i]]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isIsomorphic("egg", "add"))
    print(solution.isIsomorphic("foo", "bar"))
    print(solution.isIsomorphic("paper", "title"))
    print(solution.isIsomorphic("ab", "aa"))
