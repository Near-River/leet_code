#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.
Note: The sequence of integers will be represented as a string.
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # ret = '1'
        # for i in range(n - 1):
        #     s, _ret = ret, ''
        #     curr, count = s[0], 1
        #     for j in range(1, len(s)):
        #         if s[j] == curr:
        #             count += 1
        #         else:
        #             _ret = _ret + str(count) + curr
        #             curr = s[j]
        #             count = 1
        #     _ret = _ret + str(count) + curr
        #     ret = _ret  # update the ret
        #
        # return ret

        ret = [1]
        for i in range(n - 1):
            s, _ret = ret, []
            curr, count = s[0], 1
            for j in range(1, len(s)):
                if s[j] == curr:
                    count += 1
                else:
                    _ret.append(count)
                    _ret.append(curr)
                    curr, count = s[j], 1
            _ret.append(count)
            _ret.append(curr)
            ret = _ret  # update the ret

        return ''.join(map(str, ret))


if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(1))
    print(solution.countAndSay(3))
    print(solution.countAndSay(5))
    print(solution.countAndSay(7))
