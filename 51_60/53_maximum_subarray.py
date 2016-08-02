#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Tags: Dynamic Programming
        # solution one:
        # ret, length = nums[0], len(nums)
        # start, end = 0, length
        #
        # def maximum_sum(nums, index):
        #     if len(nums) == 1: return nums[0]
        #     ret = maximum_sum(nums[1:], index + 1)
        #     nonlocal end
        #     if ret <= 0:
        #         end = index + 1
        #         return nums[0]
        #     else:
        #         return nums[0] + ret
        #
        # while start < end:
        #     ret = max(maximum_sum(nums[start:end], start), ret)
        #     temp = nums[start]
        #     start += 1
        #     if temp <= 0:
        #         while start < length and nums[start] <= temp: start += 1
        #     else:
        #         while start < length and nums[start] <= 0: start += 1
        # return ret

        # solution two: O(N)
        length, ret = len(nums), nums[0]
        start, _sum = 0, 0
        while start < length:
            _sum += nums[start]
            ret = max(ret, _sum)
            if _sum <= 0:
                start += 1
                _sum = 0
            else:
                while _sum > 0 and start < length - 1:
                    start += 1
                    _sum += nums[start]
                    ret = max(ret, _sum)
                if _sum <= 0:
                    start += 1
                    _sum = 0
                else:
                    break
        # return ret

        # solution three: O(N)
        length, ret = len(nums), nums[0]
        _sum = 0
        for i in range(length):
            if _sum < 0: _sum = 0
            _sum += nums[i]
            ret = max(ret, _sum)
        # return ret

        # solution two: Divide and Conquer
        ret = nums[0]

        def find_minimum_sum(nums):
            nonlocal ret
            length = len(nums)
            if length == 1: return nums[0]
            if length == 2:
                if sum(nums) <= 0: ret = max(ret, max(nums))
                return sum(nums)
            mid = (len(nums) - 1) // 2
            left, right = find_minimum_sum(nums[:mid + 1]), find_minimum_sum(nums[mid + 1:])
            if left > 0 and right > 0:
                return left + right
            else:
                return max(left, right)

        ret = max(find_minimum_sum(nums), ret)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([1]))
    print(solution.maxSubArray([-1, -2]))
    print(solution.maxSubArray([-1, -2]))
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solution.maxSubArray([8, -19, 5, -4, 20]))
