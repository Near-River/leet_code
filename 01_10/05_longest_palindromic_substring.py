#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if s == '' or s.strip() == '' or len(s) == 1: return s

        # Solution one
        def isPalindrome(s):
            """
            :param s: str
            :return: boolean
            """
            return s[::-1] == s

        count = length
        while count > 0:
            for i in range(length - count + 1):
                if isPalindrome(s[i:count + i]):
                    return s[i:count + i]
            count -= 1

        # Solution two
        lst1, lst2 = [], []
        substr1, substr2 = '', ''
        for i in range(length):
            if i < length - 1 and s[i] == s[i + 1]: lst1.append(i)
            if i < length - 2 and s[i] == s[i + 2]: lst2.append(i)

        for i in lst1:
            substr = s[i:i + 2]
            x = min(i, length - i - 2)
            for j in range(1, x + 1):
                if s[i - j] != s[i + 1 + j]: break
                substr = s[i - j:i + 2 + j]
            substr1 = substr1 if len(substr1) > len(substr) else substr
        for i in lst2:
            substr = s[i:i + 3]
            x = min(i, length - i - 3)
            for j in range(1, x + 1):
                if s[i - j] != s[i + 2 + j]: break
                substr = s[i - j:i + 3 + j]
            substr2 = substr2 if len(substr2) > len(substr) else substr
        res = substr1 if len(substr1) > len(substr2) else substr2

        # Solution three
        def find_parlindrome(index):
            substr1, substr2 = '', ''
            i = j = index
            while i >= 0 and j < length:
                if s[i] != s[j]: break
                substr1 = s[i:j + 1]
                i, j = i - 1, j + 1

            i, j = index, index + 1
            while i >= 0 and j < length:
                if s[i] != s[j]: break
                substr2 = s[i:j + 1]
                i, j = i - 1, j + 1
            return substr1 if len(substr1) >= len(substr2) else substr2

        mid = (length - 1) // 2
        i, res = 0, ''
        while 2 * (mid - i + 1) >= len(res) and 2 * (length - mid - i) >= len(res):
            substr1 = find_parlindrome(mid + i)
            substr2 = find_parlindrome(mid - i)
            res = substr1 if len(substr1) >= len(substr2) else substr2
            i += 1

        # Solution four
        def expandAroundCenter(left, right):
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # return the length of the palindrome

        start, end = 0, 0
        for i in range(length):
            _len = max(expandAroundCenter(i, i), expandAroundCenter(i, i + 1))
            if _len > end - start:
                start = i - (_len - 1) // 2
                end = i + _len // 2
        res = s[start:end + 1]

        return res

    def longestPalindrome2(self, s):
        """
        Manacher's Algorithm
        """
        if s == '' or s.strip() == '' or len(s) == 1: return s

        # transform s into T
        T = '`' + ''.join(['#' + x for x in s]) + '#$'
        P = []  # An array store intermediate result, where P[i] equals to the length of the palindrome centers at Ti.
        length = len(T)
        for i in range(length): P.append(0)
        C, R = 0, 0  # C : center pointer     R : the rightmost position around the center( C )
        for i in range(1, length - 1):
            i_marror = 2 * C - i  # equals to i' = C -(i-C)

            """
            Kernel skill:
            if P[ i’] ≤ R – i
                then P[ i ] >= P[ i’] --> P[ i ] ← P[ i’]
            else
                P[ i ] ≥ R - i --> P[ i ] ← R - i
            (Which we have to expand past the right edge (R) to find P[i].
           """
            P[i] = min(R - i, P[i_marror]) if R > i else 0

            # attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            # if palindrome centered at i expand past R, adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # find the maximum element in P
        maxLen = max(P)
        centerIndex = P.index(maxLen)
        start = (centerIndex - maxLen) // 2
        return s[start:start + maxLen]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome2('abbdeaba'))
    print(solution.longestPalindrome2('aaaa'))
    print(solution.longestPalindrome2('ccc'))
    print(solution.longestPalindrome2('bb'))
