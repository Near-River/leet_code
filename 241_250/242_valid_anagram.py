#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note: You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashMap = {}
        for c in s: hashMap[c] = hashMap.get(c, 0) + 1
        for c in t:
            if c not in hashMap: return False
            hashMap[c] -= 1
            if hashMap[c] == 0: del hashMap[c]
        return len(hashMap) == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram(s="anagram", t="nagaram"))
