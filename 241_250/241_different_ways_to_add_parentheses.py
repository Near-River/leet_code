#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to
group numbers and operators. The valid operators are +, - and *.

Example 1
Input: "2-1-1".
((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]

Example 2
Input: "2*3-4*5"
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""


class Solution(object):
    def diffWaysToCompute(self, s):
        """
        :type input: str
        :rtype: List[int]
        """
        # Tags: Divide and Conquer
        opers, nums = [], []
        i = 0
        while i < len(s):
            if s[i] in ('*', '+', '-'):
                opers.append(s[i])
                i += 1
            else:
                j = i + 1
                while j < len(s) and s[j].isdigit(): j += 1
                nums.append(int(s[i:j]))
                i = j

        def do_calculate(s0, e0):
            if s0 == e0 + 1: return [nums[s0]]
            ret = []
            for i in range(s0, e0 + 1):
                oper = opers[i]
                lst1, lst2 = do_calculate(s0, i - 1), do_calculate(i + 1, e0)
                for a in lst1:
                    for b in lst2:
                        if oper == '+':
                            ret.append(a + b)
                        elif oper == '-':
                            ret.append(a - b)
                        elif oper == '*':
                            ret.append(a * b)
            return ret

        return do_calculate(0, len(opers) - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.diffWaysToCompute("2-1-1"))
    print(solution.diffWaysToCompute("2*3-4*5"))
