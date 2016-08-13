#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.
You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
"""


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution one
        nums = sorted(nums)
        gap = 0
        for i in range(len(nums) - 1, 0, -1):
            gap = max(gap, nums[i] - nums[i - 1])
        # return gap

        """
            Suppose there are N elements and they range from A to B.
            Then the maximum gap will be no smaller than ceiling[(B - A) / (N - 1)]
            Let the length of a bucket to be len = ceiling[(B - A) / (N - 1)], then we will have at most
            num = (B - A) / len + 1 of bucket

            for any number K in the array, we can easily find out which bucket it belongs by calculating
            loc = (K - A) / len and therefore maintain the maximum and minimum elements in each bucket.

            Since the maximum difference between elements in the same buckets will be at most len - 1, so the
            final answer will not be taken from two elements in the same buckets.

            For each non-empty buckets p, find the next non-empty buckets q, then q.min - p.max could be the
            potential answer to the question. Return the maximum of all those values.
       """
        if len(nums) < 2: return 0
        A, B, N = min(nums), max(nums), len(nums)
        bucket_size = (B - A) // (N - 1) if (B - A) % (N - 1) == 0 else (B - A) // (N - 1) + 1
        if bucket_size == 0: return 0
        bucket_num = (B - A) // bucket_size + 1
        buckets = [[] for i in range(bucket_num)]
        bucket_mins = [0 for i in range(bucket_num)]
        bucket_maxs = [0 for i in range(bucket_num)]

        for k in nums:
            idx = (k - A) // bucket_size
            if not buckets[idx]:
                buckets[idx].append(k)
                bucket_mins[idx] = bucket_maxs[idx] = k
            else:
                bucket_mins[idx] = min(bucket_mins[idx], k)
                bucket_maxs[idx] = max(bucket_maxs[idx], k)

        _min, _max = bucket_mins[0], bucket_maxs[0]
        gap = _max - _min
        for i in range(1, bucket_num):
            if not buckets[i]: continue
            _min2, _max2 = bucket_mins[i], bucket_maxs[i]
            gap = max(gap, _min2 - _max)
            _min, _max = _min2, _max2
        return gap


if __name__ == '__main__':
    solution = Solution()
    lst = [9, 7, 5, 12, 1, 4, 21, 3]
    print(solution.maximumGap(lst))
