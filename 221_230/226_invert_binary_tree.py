#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Invert a binary tree.
     4
   /   \
  2     7
 / \   / \
1   3 6   9

to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None: return root

        if root.left is None and root.right is None: return root
        if root.left: root.left = self.invertTree(root.left)
        if root.right: root.right = self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root


if __name__ == '__main__':
    solution = Solution()
