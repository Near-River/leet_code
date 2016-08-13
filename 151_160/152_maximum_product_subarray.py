#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        dp[i][j] = max{ ∏nums[k] (i2<=k<=j2) }, i2>=i & j2<=j
        """
        # solution one: Memory Limit Exceeded
        # length = len(nums)
        # dp = [[0] * length for i in range(length)]
        # flag = [[-1] * length for i in range(length)]  # mark ∏nums[k] (i<=k<=j) as positive or negative
        # for i in range(length):
        #     dp[i][i] = nums[i]
        #     if nums[i] > 0:
        #         flag[i][i] = 1
        #     elif nums[i] < 0:
        #         flag[i][i] = -1
        #     else:
        #         flag[i][i] = 0
        # for c in range(length - 2, -1, -1):
        #     for i in range(c + 1):
        #         j = length - 1 - c + i
        #         if flag[i][j - 1] * nums[j] > 0:
        #             flag[i][j], dp[i][j] = 1, 1
        #             for k in range(j, i - 1, -1):
        #                 if nums[k] == 0: break
        #                 dp[i][j] *= nums[k]
        #         elif flag[i][j - 1] * nums[j] == 0:
        #             if nums[j] > 0:
        #                 flag[i][j] = 1
        #             elif nums[j] < 0:
        #                 flag[i][j] = -1
        #             else:
        #                 flag[i][j] = 0
        #         dp[i][j] = max(dp[i][j - 1], dp[i + 1][j], dp[i][j])
        # return dp[0][-1]

        # solution two: Time Limit Exceeded
        length = len(nums)
        ret = -1 << 31
        dp = [[1] * length for i in range(length)]
        for i in range(length): dp[i][i] = nums[i]
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = nums[j] * dp[i][j - 1]
                ret = max(ret, dp[i][j])
        # return ret

        # solution three
        """
        max_local[i + 1] = Max(Max(max_local[i] * A[i], A[i]),  min_local * A[i])
        min_local[i + 1] = Min(Min(max_local[i] * A[i], A[i]),  min_local * A[i])
        """
        length, ret = len(nums), nums[0]
        min_local = max_local = nums[0]
        for i in range(1, length):
            _min = min_local * nums[i]
            _max = max_local * nums[i]
            _min, _max = min(_min, _max, nums[i]), max(_min, _max, nums[i])
            min_local, max_local = _min, _max
            ret = max(ret, max_local)

        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct([2, 3, -2, 4]))
    print(solution.maxProduct([-2, -3, -2, -4]))
    print(solution.maxProduct([-3, 0, -2, 1, -2]))
    print(solution.maxProduct([-3, 2, -2, 1, -1, 0, -3, -1]))
