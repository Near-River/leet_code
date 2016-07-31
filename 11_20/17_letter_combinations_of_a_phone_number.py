#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phones = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": " "
        }

        def find_all_combinations(digits):
            ret = []
            if len(digits) == 1:
                for p in phones[digits]: ret.append(p)
                return ret
            _ret = find_all_combinations(digits[1:])
            s = phones[digits[0]]
            if s == '': return _ret
            for c in s:
                for r in _ret: ret.append(c + r)
            return ret

        if digits == '': return []
        return find_all_combinations(digits)


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations(''))
    print(solution.letterCombinations('2'))
    print(solution.letterCombinations('23'))
