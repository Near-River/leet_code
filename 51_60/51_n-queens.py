#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.'
both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:
[
    [".Q..",  # Solution 1
     "...Q",
     "Q...",
     "..Q."],
    ["..Q.",  # Solution 2
     "Q...",
     "...Q",
     ".Q.."]
]
"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        """
        任意两个皇后都不能处于同一行、同一列或同一斜线上
        """
        # solution one
        # ret = []
        #
        # def findNqueens(locations, level):
        #     if level == n:  # one solution
        #         board = ['.' * n for i in range(n)]
        #         for loc in locations:
        #             s = board[loc[0]]
        #             board[loc[0]] = s[:loc[1]] + 'Q' + s[loc[1] + 1:]
        #         ret.append(board)
        #     for i in range(n):  # 任意两个皇后都不能处于同一行
        #         flag = False
        #         for loc in locations:
        #             if loc[1] == i:  # 任意两个皇后都不能处于同一列
        #                 flag = True
        #                 break
        #             x, y = loc
        #             while x + 1 < n and y + 1 < n:  # 任意两个皇后都不能处于同一斜线上
        #                 x, y = x + 1, y + 1
        #                 if x == level and i == y:
        #                     flag = True
        #                     break
        #             if flag: break
        #             x, y = loc
        #             while x - 1 >= 0 and y - 1 >= 0:
        #                 x, y = x - 1, y - 1
        #                 if x == level and i == y:
        #                     flag = True
        #                     break
        #             if flag: break
        #             x, y = loc
        #             while x - 1 >= 0 and y + 1 < n:
        #                 x, y = x - 1, y + 1
        #                 if x == level and i == y:
        #                     flag = True
        #                     break
        #             if flag: break
        #             x, y = loc
        #             while x + 1 < n and y - 1 >= 0:
        #                 x, y = x + 1, y - 1
        #                 if x == level and i == y:
        #                     flag = True
        #                     break
        #             if flag: break
        #         if flag: continue
        #         findNqueens(locations + [(level, i)], level + 1)
        #
        # findNqueens(locations=[], level=0)
        # return ret

        # solution two
        ret = []
        if 2 <= n <= 3: return []

        def findNqueens(locations, level):
            if level == n:  # one solution
                board = ['.' * n for i in range(n)]
                for loc in locations:
                    s = board[loc[0]]
                    board[loc[0]] = s[:loc[1]] + 'Q' + s[loc[1] + 1:]
                ret.append(board)
            for i in range(n):  # 任意两个皇后都不能处于同一行
                flag = False
                for loc in locations:
                    x, y = loc
                    if y == i or abs(x - level) == abs(y - i):  # 任意两个皇后都不能处于同一列或同一斜线上
                        flag = True
                        break
                if flag: continue
                findNqueens(locations + [(level, i)], level + 1)

        findNqueens(locations=[], level=0)
        # return ret

        # solution three
        ret, upperLimit = [], (1 << n) - 1

        def getQueenInfo(p):
            col = 0
            while not (p & 1):
                p >>= 1
                col += 1
            s = ['.' for i in range(n - 1)]
            s.insert(col, 'Q')
            return ''.join(s)

        def findNqueens2(row, ld, rd, cur):
            """
            :param row: 列限制条件
            :param ld: 左对角线限制条件
            :param rd: 右对角线限制条件
            :param cur: 当前放置状态
            """
            if row != upperLimit:
                pos = upperLimit & (~(row | ld | rd))  # pos中二进制为1的位，表示可以在当前行的对应列放皇后
                # 和upperLimit作与运算，主要是ld在上一层是通过左移位得到的，它的高位可能有无效的1存在，这样会清除ld高位无效的1
                while pos:
                    p = pos & (~pos + 1)  # 获取pos最右边的1,例如pos = 010110，则p = 000010
                    pos -= p  # pos最右边的1清0
                    info = getQueenInfo(p)  # 返回在当前行，即p中1对应的列放置皇后后的信息
                    findNqueens2(row | p, (ld | p) << 1, (rd | p) >> 1, cur + [info])  # 设置下一行
            else:  # one solution
                ret.append(cur)

        findNqueens2(row=0, ld=0, rd=0, cur=[])
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(4))
    print(solution.solveNQueens(8))
