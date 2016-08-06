#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:
    Did you consider the case where path = "/../"?
    In this case, you should return "/".
    Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
    In this case, you should ignore redundant slashes and return "/home/foo".
"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # solution one
        stack, i = [], 0
        while i < len(path):
            if path[i] == '/':
                start = i
                while start < len(path) and path[start] == '/': start += 1
                end = start
                while end < len(path) and path[end] != '/': end += 1
                if start < len(path):
                    word = path[start:end]
                    if word == '..':
                        if stack: stack.pop()
                    elif word != '.':
                        stack.append('/' + word)
                i = start
            i += 1

        if not stack: stack.append('/')
        # return ''.join(stack)

        # solution one
        stack, i = [], 0
        while i < len(path):
            if path[i] == '/':
                end = i + 1
                while end < len(path) and path[end] != '/': end += 1
                if end > i + 1:
                    word = path[i + 1:end]
                    if word == '..':
                        if stack: stack.pop()
                    elif word != '.':
                        stack.append('/' + word)
                    i = end - 1
            i += 1
        if not stack: stack.append('/')
        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution()
    print(solution.simplifyPath("/../"))
    print(solution.simplifyPath("/..."))
    print(solution.simplifyPath("/home/"))
    print(solution.simplifyPath("/home//foo/"))
    print(solution.simplifyPath("/a/./b/../../c/"))
