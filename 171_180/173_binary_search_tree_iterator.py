#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""


# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    # def __init__(self, root):
    #     """
    #     :type root: TreeNode
    #     """
    #     self.stack = [] if root is None else [root]
    #
    # def hasNext(self):
    #     """
    #     :rtype: bool
    #     """
    #     return len(self.stack) > 0
    #
    # def next(self):
    #     """
    #     :rtype: int
    #     """
    #     while self.stack:
    #         node = self.stack[-1]
    #         if node.left:
    #             self.stack.append(node.left)
    #             node.left = None
    #         else:
    #             if node.right: self.stack.append(node.right)
    #             self.stack.remove(node)
    #             return node.val

    def __init__(self, root):
        self.stack = []
        self.curr = root

    def hasNext(self):
        return self.curr is not None or len(self.stack) > 0

    def next(self):
        while self.curr is not None:
            self.stack.append(self.curr)
            self.curr = self.curr.left

        self.curr = self.stack.pop()
        ret = self.curr.val
        self.curr = self.curr.right
        return ret


if __name__ == '__main__':
    root = TreeNode(2)
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    root.left = node1
    root.right = node2
    iterator = BSTIterator(root)
    while iterator.hasNext():
        print(iterator.next())
