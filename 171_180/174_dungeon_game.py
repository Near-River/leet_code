#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists
of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight
his way through the dungeon to rescue the princess.
The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or
below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other
rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7.
-2 (K) 	 -3 	 3
-5 	    -10 	1
10 	    30 	   -5 (P)

Notes:
    1. The knight's health has no upper bound.
    2. Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where
    the princess is imprisoned.
"""


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # Tags: Binary Search & Dynamic Programming
        m, n = len(dungeon), len(dungeon[0])
        dp = [[1] * n for _ in range(m)]
        i = m - 1
        while i >= 0:
            j = n - 1
            while j >= 0:
                hp = 1
                if j + 1 < n and i + 1 < m:
                    hp = min(dp[i][j + 1], dp[i + 1][j])
                elif j + 1 < n:
                    hp = dp[i][j + 1]
                elif i + 1 < m:
                    hp = dp[i + 1][j]
                if dungeon[i][j] >= hp:
                    dp[i][j] = 1
                else:
                    dp[i][j] = hp - dungeon[i][j]
                j -= 1
            i -= 1
        return dp[0][0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.calculateMinimumHP([
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]))
