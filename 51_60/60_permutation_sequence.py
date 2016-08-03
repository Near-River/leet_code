#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):
    "123"
    "132"
    "213"
    "231"
    "312"
    "321"
Given n and k, return the kth permutation sequence.
Note: Given n will be between 1 and 9 inclusive.
"""


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums, factorial = [], []
        multiply = 1
        for i in range(1, n):
            multiply *= i
            nums.append(str(i))
            factorial.append(multiply)
        nums.append(str(n))

        ret, i = '', n - 1
        while i > 0:
            temp = nums[0]
            if k >= factorial[i - 1]:
                if k % factorial[i - 1] == 0:
                    temp = nums[k // factorial[i - 1] - 1]
                    nums.remove(temp)
                    ret += temp
                    ret += ''.join(nums[::-1])
                    return ret
                temp = nums[k // factorial[i - 1]]
                k %= factorial[i - 1]
            nums.remove(temp)
            ret += temp
            i -= 1
        ret += nums[0]
        return ret


if __name__ == '__main__':
    solution = Solution()
    for i in range(6):
        print(solution.getPermutation(3, i + 1))
