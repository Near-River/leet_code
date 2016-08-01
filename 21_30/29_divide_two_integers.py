#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Divide two integers without using multiplication, division and mod operator.
If it is overflow, return MAX_INT.
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # solution one
        # MAX_INT, MIN_INT = 2147483647, -2147483648
        # if divisor == 0: return MAX_INT
        # flag = 1
        # if dividend < 0:
        #     dividend = -dividend
        #     flag = -flag
        # if divisor < 0:
        #     divisor = - divisor
        #     flag = -flag
        # ret = 0
        # while dividend > divisor:  # philosophy
        #     dividend -= divisor
        #     ret += 1
        # if dividend != divisor:
        #     if ret < MAX_INT: return ret if flag == 1 else -(ret + 1)
        #     return MAX_INT if flag == 1 else MIN_INT
        # if flag == 1: return ret + 1 if ret + 1 < MAX_INT else MAX_INT
        # return -(ret + 1) if ret < MAX_INT else MIN_INT

        # solution two: Bit operating
        MAX_INT, MIN_INT = 2147483647, -2147483648
        flag = (dividend < 0) ^ (divisor < 0)  # flag == 1: return negative value
        dividend, divisor = abs(dividend), abs(divisor)
        ret = 0
        while dividend >= divisor:
            temp = divisor
            i = 1
            while dividend >= temp:
                dividend -= temp
                ret += i
                i <<= 1
                temp <<= 1
        if ret > MAX_INT and not flag: return MAX_INT
        if flag and ret > -MIN_INT: return MIN_INT
        return ret if not flag else -ret


if __name__ == '__main__':
    solution = Solution()
    # print(solution.divide(-1, 2), -1 // 2)
    # print(solution.divide(-2, 2), -2 // 2)
    # print(solution.divide(-3, 2), -3 // 2)
    # print(solution.divide(1, 2), 1 // 2)
    # print(solution.divide(2, 2), 2 // 2)
    # print(solution.divide(3, 2), 3 // 2)

    print(solution.divide(-2147483648, -1))
    print(solution.divide(-2147483648, 1))
    print(solution.divide(1004958205, -2137325331), 1004958205 // -2137325331)
    print(solution.divide(-1060849722, 99958928), -1060849722 // 99958928)
