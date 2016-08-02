#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a non-negative number represented as an array of digits , plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        n = digits[0] + 1
        carry, digits[0] = n // 10, n % 10
        i = 1
        while carry and i < len(digits):
            n = digits[i] + carry
            carry, digits[i] = n // 10, n % 10
            i += 1
        if carry: digits.append(carry)

        return digits[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne([9, 9, 9]))
    print(solution.plusOne([8, 9, 9, 9]))
