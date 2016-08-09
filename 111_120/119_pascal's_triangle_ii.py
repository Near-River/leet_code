#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1 for i in range(rowIndex + 1)]
        for i in range(3, rowIndex + 2):
            store = ret[0]
            for c in range(1, 1 + (i - 1) // 2):
                temp = ret[c]
                ret[c] = ret[i - 1 - c] = store + temp
                store = temp
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.getRow(0))
    print(solution.getRow(2))
    print(solution.getRow(3))
    print(solution.getRow(5))
