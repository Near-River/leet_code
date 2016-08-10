#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.

For example,
    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Return the sum = 12 + 13 = 25.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        self._sum = 0

        def helper(root, path):
            if root.left is None and root.right is None:
                self._sum += int(path + str(root.val))
                return
            if root.left: helper(root.left, path + str(root.val))
            if root.right: helper(root.right, path + str(root.val))

        helper(root=root, path='')
        return self._sum


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.left = node1
    root.right = node2
    node2.right = TreeNode(5)
    print(solution.sumNumbers(root))
