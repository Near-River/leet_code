#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
here are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note: The solution is guaranteed to be unique.
"""


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # solution one
        # length = len(gas)
        #
        # def doCircuit(tank, index, target):
        #     tank += gas[index] - cost[index]
        #     if tank < 0: return False
        #     index = index + 1 if index < length - 1 else 0
        #     if index == target: return True
        #     return doCircuit(tank, index, target)
        #
        # for i in range(length):
        #     if gas[i] < cost[i]: continue
        #     if doCircuit(tank=0, index=i, target=i): return i
        # return -1

        # solution two
        """
        问题变化为找到某个节点，在它之前的路段剩余油量为负， 而从它开始到整个队列结束剩余油量均不为负。
        所需时间复杂度为O(N)
       """
        # The solution is guaranteed to be unique: the aim is to find start gas station
        tank = 0
        start, left = -1, 0
        for i in range(len(gas)):
            temp = gas[i] - cost[i]
            tank += temp
            if temp >= 0:
                if start == -1:
                    start = i
                    left = temp
                else:
                    left += temp
            else:
                left += temp
                if left < 0: start = -1
        if tank < 0: return -1
        return start


if __name__ == '__main__':
    solution = Solution()
    print(solution.canCompleteCircuit([4], [6]))
    print(solution.canCompleteCircuit([2, 4], [3, 4]))
    print(solution.canCompleteCircuit([2], [2]))
    print(solution.canCompleteCircuit([2, 2], [4, 0]))
