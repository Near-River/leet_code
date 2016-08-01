#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement strStr().
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # return haystack.find(needle)
        if needle == '': return 0
        len1, len2 = len(haystack), len(needle)
        if len1 < len2: return -1
        i, j = 0, len1 - len2
        ret = -1
        while i <= j:
            if haystack[i:i + len2] == needle: return i
            if haystack[j:j + len2] == needle: ret = j
            i += 1
            j -= 1
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr('', ''))
    print(solution.strStr('', 'g'))
    print(solution.strStr('abcde', ''))
    print(solution.strStr('abcde', 'bc'))
    print(solution.strStr('abcde', 'g'))
