#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG".
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,
Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        map = {}
        i = 0
        while i + 20 <= len(s):
            for j in range(10):
                part = s[i + j:i + j + 10]
                if part in map:
                    map[part] += 1
                else:
                    map[part] = 1
            i += 10
        if i + 10 <= len(s):
            for j in range(len(s) - i - 9):
                part = s[i + j:i + j + 10]
                if part in map:
                    map[part] += 1
                else:
                    map[part] = 1
        for i in map:
            if map[i] > 1: ret.append(i)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
