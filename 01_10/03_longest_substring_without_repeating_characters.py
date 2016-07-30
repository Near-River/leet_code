#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:
    Given "abcabcbb", the answer is "abc", which the length is 3.
    Given "bbbbb", the answer is "b", with the length of 1.
    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
        "pwke" is a subsequence and not a substring.
"""

from collections import OrderedDict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # solution one: O(N**2)
        # ret, length = 0, len(s)
        # lst = list(s)
        # for i in range(length):
        #     duplicated, count = [], 0
        #     for j in range(i, length):
        #         if lst[j] in duplicated: break
        #         duplicated.append(lst[j])
        #         count += 1
        #     if count > ret: ret = count
        #
        # return ret

        # solution two - 1: O(N)
        """
        int[26] for Letters 'a' - 'z' or 'A' - 'Z'
        int[128] for ASCII
        int[256] for Extended ASCII
        """
        ret, length = 0, len(s)
        flag, start = [], 0
        for i in range(128): flag.append(False)

        for i in range(length):
            n = ord(s[i])
            if flag[n]:
                ret = max(ret, i - start)
                # the loop update the start point and reset flag array
                for j in range(start, i):
                    if s[j] == s[i]:
                        start = j + 1
                        break
                    flag[ord(s[j])] = False
            else:
                flag[n] = True
        ret = max(ret, length - start)
        # return ret

        # solution two - 2: O(N)
        # ret, index = 0, []
        # for i in range(128): index.append(0)
        # i = 0
        # for j in range(len(s)):
        #     i = max(index[ord(s[j])], i)
        #     ret = max(ret, j - i + 1)
        #     index[ord(s[j])] = j + 1
        #
        # return ret

        # solution two - 3: O(N)
        ret, d = 0, {}
        i = 0
        for j in range(len(s)):
            i = max(d.get(s[j], 0), i)
            ret = max(ret, j - i + 1)
            d[s[j]] = j + 1

        # return ret

        # solution three: > O(N)
        # ret, length = 0, len(s)
        # d, start = OrderedDict(), 0
        #
        # for i in range(length):
        #     ch = s[i]
        #     if ch in d.keys():
        #         ret = max(ret, i - start)
        #         # update the start point
        #         start = d[ch] + 1
        #         # reset the existed value dict
        #         ks, vs = list(d.keys()), list(d.values())
        #         idx, d = ks.index(ch), OrderedDict()
        #         for k, v in zip(ks[idx + 1:], vs[idx + 1:]): d[k] = v
        #         d[ch] = i
        #     d[ch] = i
        # ret = max(ret, length - start)
        # return ret

        # solution four: O(N)
        """
        Sliding Window
        """
        length, ret = len(s), 0
        st = set()  # existed value's set
        i = j = 0
        while j < length:
            if s[j] not in st:
                st.add(s[j])
                ret = max(ret, j - i + 1)
                j += 1
            else:
                st.remove(s[i])
                i += 1

        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring(""))
    print(solution.lengthOfLongestSubstring("c"))
    print(solution.lengthOfLongestSubstring("dvdf"))
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))
