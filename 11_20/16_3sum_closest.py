#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


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

from itertools import combinations


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # solution one
        ret = sum(nums[:3])
        closest = abs(ret - target)
        for t in combinations(nums, 3):
            n = abs(sum(t) - target)
            if n < closest:
                closest = n
                ret = sum(t)

        # solution two
        nums = sorted(nums)  # sorting the number list
        length, ret = len(nums), 0
        temp = abs(nums[0] + nums[1] + nums[length - 1] - target)
        for i in range(length - 2):
            first, tail = i + 1, length - 1
            while first < tail:
                _sum = nums[i] + nums[first] + nums[tail]
                if _sum > target:
                    tail -= 1
                elif _sum < target:
                    first += 1
                else:
                    return _sum
                n = abs(_sum - target)
                if n <= temp: temp, ret = n, _sum
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest(nums=[-1, 2, 1, -4], target=1))
    print(solution.threeSumClosest(nums=[1, 1, 1, 0], target=-100))
