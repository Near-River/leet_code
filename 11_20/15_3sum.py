#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]


    // 2 sum problem
    int i = starting; //头指针
    int j = num.size() - 1; //尾指针
    while(i < j) {
        int sum = num[i] + num[j];
        if(sum == target) {
            store num[i] and num[j] somewhere;
            if(we need only one such pair of numbers)
                break;
            otherwise
                do ++i, --j;
        }
        else if(sum < target)
            ++i;
        else
            --j;
    }
"""

import random


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)  # sorting the number list
        length, ret = len(nums), set()
        for i in range(length - 2):
            first, tail = i + 1, length - 1
            while first < tail:
                _sum = nums[i] + nums[first] + nums[tail]
                if _sum > 0:
                    tail -= 1
                elif _sum < 0:
                    first += 1
                else:
                    ret.add((nums[i], nums[first], nums[tail]))
                    first += 1
                    tail -= 1
        return list(map(list, ret))


if __name__ == '__main__':
    solution = Solution()
    nums = []
    for i in range(1000):
        nums.append(random.randint(-100, 100))
    print(solution.threeSum(nums=nums))
