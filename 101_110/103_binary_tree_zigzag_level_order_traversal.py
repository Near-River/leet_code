#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # solution one: Queue
        # if root is None: return []
        # ret = []
        # queue = deque()
        # queue.append(root)
        # order = True
        # while queue:
        #     values, _queue = [], deque()
        #     while queue:
        #         node = queue.popleft()
        #         values.append(node.val)
        #         if node.left is not None: _queue.append(node.left)
        #         if node.right is not None: _queue.append(node.right)
        #     if order:
        #         ret.append(values)
        #     else:
        #         ret.append(values[::-1])
        #     order = not order
        #     queue = _queue
        # return ret

        # solution two: Stack
        if root is None: return []
        ret = []
        stack = [root]
        order = True
        while stack:
            values, _stack = [], []
            while stack:
                node = stack.pop()
                values.append(node.val)
                if order:
                    if node.left is not None: _stack.append(node.left)
                    if node.right is not None: _stack.append(node.right)
                else:
                    if node.right is not None: _stack.append(node.right)
                    if node.left is not None: _stack.append(node.left)
            ret.append(values)
            order = not order
            stack = _stack
        return ret


if __name__ == '__main__':
    solution = Solution()
