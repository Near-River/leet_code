#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",
return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        """
        一个有效的IP地址由4个数字组成，每个数字在0-255之间。对于其中的2位数或3位数，不能以0开头。
        所以对于以s[i]开头的数字有3种可能：
            1. s[i]
            2. s[i : i+1]，s[i] !=0时
            3. s[i : i+2]，s[i] != 0，且s[i : i+2] <= 255
        """
        ret = []

        def findIPAddress(s, n, nums):
            if n == 0:
                if s == '':  ret.append('.'.join(nums))
                return
            length = len(s)
            if length >= 1: findIPAddress(s[1:], n - 1, nums + [s[0]])
            if length >= 2 and s[0] != '0':
                findIPAddress(s[2:], n - 1, nums + [s[:2]])
                if length >= 3:
                    if int(s[:3]) <= 255: findIPAddress(s[3:], n - 1, nums + [s[:3]])

        findIPAddress(s, 4, [])
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.restoreIpAddresses("1111"))
    print(solution.restoreIpAddresses("25525511135"))
