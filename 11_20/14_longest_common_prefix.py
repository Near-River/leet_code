#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []: return ''
        strs = sorted(sorted(strs), key=lambda x: len(x))
        s = strs[0]
        _len, i = len(s), 0
        while i < len(s):
            _s = s[:i + 1]
            for j in range(1, len(strs)):
                if not strs[j].startswith(_s): return s[:i]
            i += 1
        return s[:i + 1]


if __name__ == '__main__':
    solution = Solution()
    strs = ['abc', 'abcxyz', 'abckkk', 'ee']
    print(solution.longestCommonPrefix(strs))
    print(solution.longestCommonPrefix([]))
    print(solution.longestCommonPrefix(['abc']))
    print(solution.longestCommonPrefix(['aa', 'ab']))
