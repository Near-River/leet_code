#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == '': return 0
        ret, i = 0, len(s) - 1
        while i >= 0:
            if s[i] == ' ': break
            ret += 1
            i -= 1
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLastWord('Hello World'))
