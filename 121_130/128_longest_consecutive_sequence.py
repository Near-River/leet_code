#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Since it requires O(n) solution, normal sort won't be work here. Hash probably is the best choice.
        Three Steps:
        1. create the hashmap to hold <num, index>
        2. scan the num vector from left to right, for each num
            i, check whether num -1 is in the map  (loop)
            ii, check whether num+1 is in the map  (loop)
        3. track the sequence length during scanning.
        """
        if not nums: return 0
        length, ret = len(nums), 1
        map = {}
        for i in range(length): map[nums[i]] = True
        for n in nums:
            if n in map:
                del map[n]
                start = n - 1
                if start in map:
                    while start in map:
                        del map[start]
                        start -= 1
                end = n + 1
                if end in map:
                    while end in map:
                        del map[end]
                        end += 1
                ret = max(ret, end - start - 1)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
