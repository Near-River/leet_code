#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three",
it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:
0.1 < 1.1 < 1.2 < 13.37
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = version1.split('.'), version2.split('.')
        while len(v1) > 1 and int(v1[-1]) == 0: v1.pop()
        while len(v2) > 1 and int(v2[-1]) == 0: v2.pop()
        i = 0
        while i < len(v1) and i < len(v2):
            n1, n2 = int(v1[i]), int(v2[i])
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1
            i += 1
        if i < len(v1):
            return 1
        elif i < len(v2):
            return -1
        else:
            return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.compareVersion('1.1', '1.3'))
    print(solution.compareVersion('1.1.2', '1.1'))
    print(solution.compareVersion('1.0', '1'))
