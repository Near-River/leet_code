#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 You are given a string, s, and a list of words, words, that are all of the same length.
 Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once
 and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0, 9] (order does not matter).
"""

from copy import copy
from collections import defaultdict


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # solution one: Time Limit Exceeded
        # if not words: return []
        # N, M, K = len(s), len(words), len(words[0])
        # if N < M * K: return []
        # ret = []
        # for i in range(N - K * M + 1):
        #     _s = s[i:i + K * M]
        #     duplicated = copy(words)
        #     for j in range(M):  # optimization: Two Pointers
        #         w = _s[j * K:(j + 1) * K]
        #         if w not in duplicated: break
        #         duplicated.remove(w)
        #     if not duplicated: ret.append(i)
        #
        # return ret

        # solution two: Time Limit Exceeded
        # if not words: return []
        # N, M, K = len(s), len(words), len(words[0])
        # if N < M * K: return []
        # ret, d = [], defaultdict(int)
        # for word in words:
        #     d[word] += 1
        # for i in range(N - K * M + 1):
        #     temp, j = defaultdict(int), 0
        #     while j < M:
        #         word = s[i + j * K:i + (j + 1) * K]
        #         if word not in d.keys(): break
        #         temp[word] += 1
        #         if temp[word] > d[word]: break
        #         j += 1
        #     if j == M: ret.append(i)
        #
        # return ret

        # solution three: Sliding Window O( N * K )
        words_hash = defaultdict(int)
        for word in words: words_hash[word] += 1
        wlen, wsize = len(words), len(words[0])
        res = []

        for start in range(wsize):
            slidingWindow = defaultdict(int)
            wCount = 0  # counting the word's number in the slidering-window
            for i in range(start, len(s), wsize):
                word = s[i: i + wsize]
                if word in words_hash:
                    slidingWindow[word] += 1
                    wCount += 1
                    while words_hash[word] < slidingWindow[word]:
                        pos = i - wsize * (wCount - 1)  # the leftmost location of the sliding window
                        removeWord = s[pos: pos + wsize]
                        slidingWindow[removeWord] -= 1
                        wCount -= 1
                else:
                    slidingWindow.clear()  # clear the slidering-window and reset the word's counter
                    wCount = 0
                if wCount == wlen: res.append(i - wsize * (wCount - 1))

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.findSubstring("barfoothefoobarmanbar", ["foo", "bar"]))
    print(solution.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
    print(solution.findSubstring("ababaab", ["ab", "ba", "ba"]))
