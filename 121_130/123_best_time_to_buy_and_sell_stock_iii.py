#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""


class Solution(object):
    def maxProfit(self, prices):
        """
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
        # solution one: Dynamic Programming
        # if not prices: return 0
        # _global = [0, 0, 0]
        # _local = [0, 0, 0]
        #
        # for i in range(1, len(prices)):
        #     diff = prices[i] - prices[i - 1]
        #     _gs, _ls = [0, 0, 0], [0, 0, 0]
        #     for j in range(1, 3):
        #         _ls[j] = max(_global[j - 1] + max(diff, 0), _local[j] + diff)
        #         _gs[j] = max(_ls[j], _global[j])
        #     _global = _gs
        #     _local = _ls
        # return _global[-1]

        # optimization
        if not prices: return 0
        _global = [0] * 3
        _local = [0] * 3

        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            j = 2
            while j >= 1:
                _local[j] = max(_global[j - 1] + max(diff, 0), _local[j] + diff)
                _global[j] = max(_local[j], _global[j])
                j -= 1
        # return _global[-1]

        n = len(prices)
        if n < 2: return 0
        p1 = [0] * n
        p2 = [0] * n
        minV = prices[0]
        for i in range(1, n):
            minV = min(minV, prices[i])
            p1[i] = max(p1[i - 1], prices[i] - minV)
        maxV = prices[-1]
        for i in range(n - 2, -1, -1):
            maxV = max(maxV, prices[i])
            p2[i] = max(p2[i + 1], maxV - prices[i])
        ret = 0
        for i in range(n): ret = max(ret, p1[i] + p2[i])
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProfit([3, 2, 6, 5, 0, 3]))
    print(solution.maxProfit([6, 1, 3, 2, 4, 7]))
