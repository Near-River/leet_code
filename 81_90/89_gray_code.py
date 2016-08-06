#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code.
A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
00 - 0
01 - 1
11 - 3
10 - 2

Note:
For a given n, a gray code sequence is not uniquely defined.
For example, [0, 2, 3, 1] is also a valid gray code sequence according to the above definition.
For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
"""


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        # solution one
        def buildGrayCode(val, store):
            if len(store) == 1 << n: return True
            temp = 1
            for i in range(n):
                # transform value to a new value differ in only one bit
                new_val = val ^ temp
                temp <<= 1
                if new_val in store: continue
                store.append(new_val)
                if buildGrayCode(new_val, store): return True
                store.remove(new_val)
            return False

        sequence = [0]
        buildGrayCode(val=0, store=sequence)
        # return sequence

        # solution two
        if n == 0: return [0]
        result = self.grayCode(n - 1)
        sequence = list(result)
        for num in reversed(result):
            sequence.append((1 << (n - 1)) | num)
        return sequence


if __name__ == '__main__':
    solution = Solution()
    print(solution.grayCode(0))
    print(solution.grayCode(1))
    print(solution.grayCode(2))
    print(solution.grayCode(3))
