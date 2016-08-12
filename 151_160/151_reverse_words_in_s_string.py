#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Clarification:
    What constitutes a word?
    A sequence of non-space characters constitutes a word.
    Could the input string contain leading or trailing spaces?
    Yes. However, your reversed string should not contain leading or trailing spaces.
    How about multiple spaces between two words?
    Reduce them to a single space in the reversed string.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        lst = s.split(' ')
        lst = list(filter(lambda x: x, lst))
        s = ' '.join(lst[::-1])
        return s


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords('  cat  dog    apple  '))
