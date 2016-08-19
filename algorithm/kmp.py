#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KMP Algorithm (Knuth-Morris-Pratt)
"""


def violentMatch(s, p):
    m, n = len(s), len(p)
    if m < n: return -1
    i, j = 0, 0
    while i < m and j < n:
        if s[i] == s[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j == n: return i - j
    return -1


def KMP(s, p):
    def get_next(_next, pattern, length):
        """
        next 数组各值的含义：代表当前字符之前的字符串中，有多大长度的相同前缀后缀。
        :return:
        """
        _next[0] = -1
        k = -1
        i = 0
        while i < length - 1:
            if k == -1 or pattern[i] == pattern[k]:
                k += 1
                i += 1
                if pattern[i] != pattern[k]:
                    _next[i] = k
                else:  # avoid pattern[i] = pattern[_next[i]]
                    _next[i] = _next[k]
            else:
                k = _next[k]
        return _next

    def get_next2(_next, pattern, length):
        _next[0] = -1
        i, k = 0, -1
        while i < length - 1:
            while k >= 0 and pattern[i] != pattern[k]:
                k = _next[k]
            i += 1
            k += 1
            _next[i] = k
        return _next

    m, n = len(s), len(p)
    _next = [0] * n
    get_next(_next, p, n)
    i = j = 0
    while i < m and j < n:
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = _next[j]
    if j == n: return i - j
    return -1


if __name__ == '__main__':
    print(KMP('abacababc', 'abab'))
