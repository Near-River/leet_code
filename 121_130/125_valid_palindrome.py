#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '': return True
        i, j = 0, len(s) - 1
        while i < j:
            if not (s[i].isalpha() or s[i].isdigit()):
                i += 1
                continue
            if not (s[j].isalpha() or s[j].isdigit()):
                j -= 1
                continue
            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
