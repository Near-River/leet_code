#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    (you may want to display this pattern in a fixed font for better legibility(易读性))
(循环对角线结构)
P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
"""

from functools import reduce


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == '' or s.strip() == '': return s
        if numRows == 1: return s

        length, loop_num = len(s), 2 * (numRows - 1)
        lst = [[] for i in range(numRows)]
        count = 0
        while length >= loop_num:
            for i in range(numRows):
                lst[i].append(s[count * loop_num + i])
                if i != 0 and i != (numRows - 1):
                    lst[i].append(s[count * loop_num + 2 * (numRows - 1) - i])
            length -= loop_num
            count += 1
        if length:
            for i in range(length):
                if i >= numRows: break
                lst[i].append(s[count * loop_num + i])
                if i != 0 and i != (numRows - 1) and 2 * numRows - 1 - i <= length:
                    lst[i].append(s[count * loop_num + 2 * (numRows - 1) - i])
        s = reduce(lambda s1, s2: s1 + s2, (map(lambda l: ''.join(l), lst)))

        return s


if __name__ == '__main__':
    solution = Solution()
    print(solution.convert(s='abcdefg', numRows=5))
