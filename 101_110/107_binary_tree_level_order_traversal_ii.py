#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3, 9, 20, null, null, 15, 7],
    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:
[
    [15, 7],
    [9, 20],
    [3]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        valueStack = []
        queue = deque()
        queue.append(root)
        while queue:
            values, _queue = [], deque()
            while queue:
                node = queue.popleft()
                values.append(node.val)
                if node.left: _queue.append(node.left)
                if node.right: _queue.append(node.right)
            valueStack.insert(0, values)
            queue = _queue

        return valueStack


if __name__ == '__main__':
    solution = Solution()
