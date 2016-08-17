#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used
and each combination should be a unique set of numbers.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.ret = []

        def helper(count, target, start, path):
            if count == 0:
                if target != 0: return
                self.ret.append(path + [])
            if start > target: return
            for i in range(start + 1, 10):
                path.append(i)
                helper(count - 1, target - i, i, path)
                path.pop()

        helper(k, n, 0, [])
        return self.ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum3(3, 7))
    print(solution.combinationSum3(3, 9))
