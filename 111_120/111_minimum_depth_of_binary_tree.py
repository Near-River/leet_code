#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        min_depth, stack = 1, [root]
        while stack:
            _stack = []
            while stack:
                node = stack.pop()
                if node.left is None and node.right is None: return min_depth
                if node.left: _stack.append(node.left)
                if node.right: _stack.append(node.right)
            stack = _stack
            min_depth += 1
        return min_depth


if __name__ == '__main__':
    solution = Solution()
