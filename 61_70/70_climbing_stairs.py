#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # solution: recursive(Time Limit Exceeded)
        def find_walk_ways(length):
            if length <= 0: return length + 1
            return find_walk_ways(length - 1) + find_walk_ways(length - 2)

        # return find_walk_ways(n)

        # solution two: Fibonacci sequence 1 1 2 3 5 8 13 21 ...
        a, b = 1, 1
        for i in range(n - 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    solution = Solution()
    for i in range(1, 6):
        print(solution.climbStairs(i))
    print(solution.climbStairs(35))
