#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Determine whether an integer is a palindrome. Do this without extra space.
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x < 0: return False
        # return x == int(str(x)[::-1])

        if x < 0: return False
        if x < 10: return True
        base = 1
        while x // base > 10:
            base *= 10
        while x:
            left, right = x // base, x % 10
            if left != right: return False
            x -= base * left
            x //= 10
            base //= 100
        return True


if __name__ == '__main__':
    solution = Solution()
    # print(solution.isPalindrome(103))
    print(solution.isPalindrome(12321))
    print(solution.isPalindrome(-43234))
