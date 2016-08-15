#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
"""


class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # solution one
        binary = ''
        temp = 1
        for i in range(32):
            binary += '1' if n & temp != 0 else '0'
            temp <<= 1
        ret = int(binary, 2)
        # return ret

        # solution two
        ret = 0
        for i in range(32):
            ret = ret << 1 | (n & 1)
            n >>= 1
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseBits(43261596))
