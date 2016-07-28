#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.
For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
    [
      [-1,  0, 0, 1],
      [-2, -1, 1, 2],
      [-2,  0, 0, 2]
    ]
"""

import random


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # solution one
        nums = sorted(nums)  # sorting the number list
        length, d = len(nums), {}
        for i in range(length - 1):
            for j in range(i + 1, length):
                _sum = nums[i] + nums[j]
                try:
                    d[_sum]
                except KeyError:
                    d[_sum] = []
                d[_sum].append([i, j])
        ret = []
        for i in range(length - 3):
            if i != 0 and nums[i] == nums[i - 1]: continue  # 排除结果集第一个元素的重复值
            for j in range(i + 1, length - 2):
                if j != i + 1 and nums[j] == nums[j - 1]: continue  # 排除结果集第二个元素的重复值
                res = target - nums[i] - nums[j]
                if res in d.keys():
                    lst = d[res]
                    _len,isFirstPush = len(lst), True
                    for k in range(_len):
                        if lst[k][0] <= j: continue  # 保证所求的四元组的数组下标是递增的
                        # 同一个链表中的二元对两个元素的和都是相同的，因此只要两个二元对的一个元素不同，则这两个二元对就不同
                        if isFirstPush or nums[lst[k][0]] > ret[len(ret) - 1][2]:
                            ret.append([nums[i], nums[j], nums[lst[k][0]], nums[lst[k][1]]])
                            isFirstPush = False

        # solution two
        nums = sorted(nums)  # sorting the number list
        length, d = len(nums), dict()
        for i in range(length - 1):
            for j in range(i + 1, length):
                _sum = nums[i] + nums[j]
                try:
                    d[_sum]
                except KeyError:
                    d[_sum] = []
                d[_sum].append([i, j])
        ret = []
        ks = sorted(d.keys())
        for k in ks:
            sum2 = target - k
            if sum2 < k: continue
            if sum2 in ks:
                for (i1, j1) in d[k]:
                    for (i2, j2) in d[sum2]:
                        temp = {i1, j1, i2, j2}
                        if len(temp) == 4:
                            lst = sorted([nums[i1], nums[i2], nums[j1], nums[j2]])
                            if lst not in ret: ret.append(lst)

        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
    print(solution.fourSum(nums=[1, -2, -5, -4, -3, 3, 3, 5], target=-11))
    print(solution.fourSum(nums=[1, 4, -3, 0, 0, 0, 5, 0], target=0))
    print(solution.fourSum(nums=[0, 2, 2, 2, 10, -3, -9, 2, -10, -4, -9, -2, 2, 8, 7], target=6))

    nums = []
    for i in range(100):
        nums.append(random.randint(-100, 100))
    print(solution.fourSum(nums=nums, target=21))
