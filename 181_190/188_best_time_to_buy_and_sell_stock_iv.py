#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        """
        使用“局部最优和全局最优解法”
        我们维护两种变量，一个是当前到达第i天可以最多进行j次交易，最好的利润是多少（global[i][j]），
        另一个是当前到达第i天，最多可进行j次交易，并且最后一次交易在当天卖出的最好的利润是多少（local[i][j]）

        递推式:
            global[i][j] = max(local[i][j], global[i-1][j])
            local[i][j] = max(global[i-1][j-1] + max(diff, 0), local[i-1][j] + diff)
                (注：diff = prices[i] - prices[i-1])
        """
        # solution one: Time Limit Exceeded
        if k < 1 or not prices: return 0
        if k >= len(prices):
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]: profit += prices[i] - prices[i - 1]
            return profit
        _global = [0] * (k + 1)
        _local = [0] * (k + 1)
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            for j in range(k, 0, -1):
                _local[j] = max(_global[j - 1] + max(diff, 0), _local[j] + diff)
                _global[j] = max(_local[j], _global[j])
        return _global[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit(2, [6, 1, 3, 2, 4, 7]))
