#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement atoi to convert a string to an integer.

Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect
on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because
either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values,
INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

"""


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == '': return 0

        flag = True
        INT_MAX, INT_MIN = 2147483647, -2147483648

        if s.startswith('+'):
            s = s[1:]
        elif s.startswith('-'):
            flag = False
            s = s[1:]

        for i, v in enumerate(s):
            try:
                int(v)
            except Exception as e:
                s = s[:i]
                break

        if s == '': return 0
        res = int(s) if flag else -1 * int(s)
        if res < INT_MIN: return INT_MIN
        if res > INT_MAX: return INT_MAX

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi('-123abc'))
    print(solution.myAtoi('+123a123'))
    print(solution.myAtoi(''))
