#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a binary tree
    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Note:
    You may only use constant extra space.
    You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7

After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""


# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        # solution one
        # if root is None: return
        # array = [root]
        # while array:
        #     _array = []
        #     curr = array[0]
        #     if curr.left: _array.append(curr.left)
        #     if curr.right: _array.append(curr.right)
        #     for i in range(1, len(array)):
        #         node = array[i]
        #         if node.left: _array.append(node.left)
        #         if node.right: _array.append(node.right)
        #         curr.next = array[i]
        #         curr = curr.next
        #     array = _array

        # solution two
        if root is None: return
        first = root
        while True:
            if not first.left: break
            first.left.next = first.right
            if first.next:
                curr = first
                while curr.next:
                    curr.right.next = curr.next.left
                    curr = curr.next
                    curr.left.next = curr.right
            first = first.left

        # solution three: Best
        if root is None: return
        curr = root
        first = None
        while True:
            if first is None: first = curr.left
            if not curr.left: break
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
                curr = curr.next
            else:
                curr = first
                first = None


if __name__ == '__main__':
    solution = Solution()
