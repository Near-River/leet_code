#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions
at the same time (ie, you must sell the stock before you buy again).
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length < 2: return 0
        profit = 0
        # you must sell the stock before you buy again
        start = -1
        for i in range(length - 1):
            if prices[i] <= prices[i + 1]:
                if start == -1: start = i
            elif start != -1:
                profit += prices[i] - prices[start]
                start = -1
        if start != -1: profit += prices[-1] - prices[start]
        return profit


if __name__ == '__main__':
    solution = Solution()
