#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:
[
    ["ate", "eat", "tea"],
    ["nat", "tan"],
    ["bat"]
]

Note: All inputs will be in lower-case.
"""

from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words = defaultdict(list)
        for s in strs: words[''.join(sorted(s))].append(s)

        return list(words.values())


if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
