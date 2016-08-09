#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given
         1
        / \
       2   5
      / \   \
     3   4   6

The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
Hints:
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None: return
        curr = root
        stack = []
        while True:
            if curr.left:
                if curr.right: stack.append(curr.right)
                curr.right = curr.left
                curr.left = None
                curr = curr.right
            elif curr.right:
                curr = curr.right
            else:
                if not stack: break
                curr.right = stack.pop()
                curr = curr.right


if __name__ == '__main__':
    solution = Solution()
