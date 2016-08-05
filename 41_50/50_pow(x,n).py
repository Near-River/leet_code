#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement pow(x, n).
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1.0
        flag, n = n > 0, abs(n)

        def pow(x, n):
            if n == 1: return x
            v = pow(x, n >> 1)
            if n % 2 == 1:
                return x * v * v
            else:
                return v * v

        ret = pow(x, n)
        return ret if flag else 1.0 / ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(20, 2))
    print(solution.myPow(0.00001, 2147483647))
    print(solution.myPow(34.00515, -3))
    print(solution.myPow(2.00000, -2147483648))
