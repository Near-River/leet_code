#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Follow up for N-Queens problem.
Now, instead outputting board configurations, return the total number of distinct solutions.
"""


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        upperLimit = (1 << n) - 1

        def findNqueens2(row, ld, rd):
            """
            :param row: 列限制条件
            :param ld: 左对角线限制条件
            :param rd: 右对角线限制条件
            """
            ret = 0
            if row != upperLimit:
                pos = upperLimit & (~(row | ld | rd))  # pos中二进制为1的位，表示可以在当前行的对应列放皇后
                while pos:
                    p = pos & (~pos + 1)  # 获取pos最右边的1,例如pos = 010110，则p = 000010
                    pos -= p  # pos最右边的1清0
                    ret += findNqueens2(row | p, (ld | p) << 1, (rd | p) >> 1)  # 设置下一行
                return ret
            else:  # one solution
                return 1

        return findNqueens2(row=0, ld=0, rd=0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.totalNQueens(4))
    print(solution.totalNQueens(8))