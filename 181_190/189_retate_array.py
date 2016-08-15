#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note: Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Hint: Could you do it in-place with O(1) extra space?
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 1: return
        if k >= n: k %= n
        if k < 1: return

        _len, _s = n, 0
        while True:
            if k <= _len // 2:
                while k <= _len // 2:
                    _e = _len + _s
                    for i in range(1, k + 1): nums[_e - i], nums[_e - i - k] = nums[_e - i - k], nums[_e - i]
                    _len -= k
                    if _len == k or k == 0: return
            else:
                while k > _len // 2:
                    m = _len - k
                    for i in range(m): nums[_s + i], nums[_s + m + i] = nums[_s + m + i], nums[_s + i]
                    k -= m
                    _s += m
                    _len -= m


if __name__ == '__main__':
    solution = Solution()
    lst, lst2 = [], []
    for i in range(1, 11): lst.append(i)
    for i in range(1, 10): lst2.append(i)
    i = 3
    print(solution.rotate(lst, i))
    print(solution.rotate(lst2, i))
