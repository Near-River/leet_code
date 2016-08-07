#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # solution one: Time Limit Exceeded
        # nums = [i for i in range(1, n + 1)]
        #
        # def buildBFS(nums):
        #     if not nums: return 1
        #     count = 0
        #     for i in range(len(nums)):
        #         count += buildBFS(nums[:i]) * buildBFS(nums[i + 1:])
        #     return count
        #
        # return buildBFS(nums)

        # if n == 0: return 1
        # ret = 0
        # for i in range(1, n + 1):
        #     ret += self.numTrees(n - i) * self.numTrees(i - 1)
        # return ret

        # solution two
        if n <= 1: return 1
        array = [1, 1]
        for i in range(2, n + 1):
            m = 0
            for j in range(i // 2): m += 2 * array[j] * array[i - j - 1]
            if i % 2 == 1: m += array[i // 2] * array[i // 2]
            array.append(m)
        return array[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numTrees(3))
    print(solution.numTrees(4))
    print(solution.numTrees(5))
    print(solution.numTrees(13))
    print(solution.numTrees(19))
