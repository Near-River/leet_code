#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5
max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0
In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # solution one
        # profit = 0
        #
        # for i in range(len(prices) - 1):
        #     buy = prices[i]
        #     sell = max(prices[i + 1:])
        #     if sell > buy: profit = max(profit, sell - buy)
        #
        # return profit

        # solution two
        length = len(prices)
        if length < 2: return 0
        profit = 0
        i = length - 2
        sell = prices[-1]
        while i >= 0:
            buy = prices[i]
            if buy < sell:
                profit = max(profit, sell - buy)
            else:
                sell = buy
            i -= 1

        return profit


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit([7, 6, 4, 3, 1]))
