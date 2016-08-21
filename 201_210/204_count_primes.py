#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Description:
Count the number of prime numbers less than a non-negative number, n.
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        # solution one
        # def isPrime(n):
        #     if n <= 1: return False
        #     i = 2
        #     while i ** 2 < n:
        #         if n % i == 0: return False
        #         i += 1
        #     return True
        #
        # count = 0
        # for i in range(1, n):
        #     if isPrime(i): count += 1
        # return count

        # solution two: Sieve of Eratosthenes
        if n <= 2: return 0
        isPrime = [True] * n
        i = 2
        while i ** 2 < n:
            if isPrime[i - 2]:
                j = i * i
                while j < n:
                    isPrime[j] = False
                    j += i
            i += 1
        count = 0
        for i in isPrime:
            if i: count += 1
        return count - 2


if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrimes(1500000))
