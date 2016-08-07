#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3, 9, 20, null, null, 15, 7],
    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:
[
    [3],
    [9, 20],
    [15, 7]
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        ret = []
        queue = deque()
        queue.append(root)
        while queue:
            values, _queue = [], deque()
            while queue:
                node = queue.popleft()
                values.append(node.val)
                if node.left is not None: _queue.append(node.left)
                if node.right is not None: _queue.append(node.right)
            ret.append(values)
            queue = _queue
        return ret


if __name__ == '__main__':
    solution = Solution()
