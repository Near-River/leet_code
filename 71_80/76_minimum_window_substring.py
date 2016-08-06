#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""

from collections import defaultdict


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # solution one
        charDict = defaultdict(int)
        for ch in t: charDict[ch] += 1
        len1, len2 = len(s), len(t)
        minWindow, ret = len1 + 1, ''
        d = defaultdict(list)
        d_len, d_lst = 0, []
        for i in range(len1):
            if s[i] in t:
                ch = s[i]
                if len(d[ch]) == charDict[ch]:
                    idx = d[ch].pop(0)
                    d_lst.remove(idx)
                else:
                    if d_len < len2: d_len += 1
                d[ch].append(i)
                d_lst.append(i)
                if d_len == len2 and d_lst[-1] - d_lst[0] + 1 < minWindow:
                    minWindow = d_lst[-1] - d_lst[0] + 1
                    ret = s[d_lst[0]:d_lst[-1] + 1]
        if d_len < len2: return ''
        # return ret

        # solution two
        if s == '' or t == '': return ''
        charDict = dict.fromkeys(t, 0)
        for ch in t: charDict[ch] += 1
        ret, count = '', 0
        start = 0
        d = dict.fromkeys(t, 0)
        for i in range(len(s)):
            if s[i] in charDict:
                ch = s[i]
                if d[ch] < charDict[ch]: count += 1
                d[ch] += 1
            if count == len(t):
                while start < i:
                    if s[start] in charDict:
                        if d[s[start]] == charDict[s[start]]: break
                        d[s[start]] -= 1
                    start += 1
                if ret == '' or i - start + 1 < len(ret): ret = s[start:i + 1]
                # abandon the leftmost element
                d[s[start]] -= 1
                count -= 1
                start += 1

        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.minWindow(s="a", t=""))
    print(solution.minWindow(s="a", t="aa"))
    print(solution.minWindow(s="aa", t="aa"))
    print(solution.minWindow(s="bba", t="ab"))
    print(solution.minWindow(s="ADOBECODEBANC", t="ABC"))
