#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully
(left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces
' ' when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide
evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.
Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
"""


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        n = len(words)
        i, ret = 0, []
        while i < n:
            _len = len(words[i])
            j = i + 1
            while j < n and _len + 1 + len(words[j]) <= maxWidth:
                _len += (1 + len(words[j]))
                j += 1
            line = words[i]
            if j < n:
                solts = j - i - 1
                spaceNum = maxWidth - _len + solts
                if solts > 0:
                    for k in range(1, solts + 1):
                        c = spaceNum // solts if spaceNum % solts == 0 else spaceNum // solts + 1
                        spaceNum -= c
                        solts -= 1
                        line += ' ' * c
                        line += words[i + k]
                else:
                    line += ' ' * spaceNum
            else:
                for k in range(1, j - i): line += (' ' + words[i + k])
                line += ' ' * (maxWidth - _len)
            ret.append(line)
            i = j
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.fullJustify(["Listen", "to", "many,", "speak", "to", "a", "few."], 6))
    print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
