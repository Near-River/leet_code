#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Follow up for problem "Populating Next Right Pointers in Each Node".
What if the given tree could be any binary tree? Would your previous solution still work?

Note: You may only use constant extra space.

For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7

After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
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
        if root is None: return
        curr = root
        first = None
        prev = None
        while True:
            if curr.left:
                if first is None: first = curr.left
                if prev is None:
                    prev = curr.left
                else:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
            elif curr.right:
                if first is None: first = curr.right
                if prev is None:
                    prev = curr.right
                else:
                    prev.next = curr.right
                    prev = prev.next
            if curr.next:
                curr = curr.next
            else:
                if first is None: break
                curr = first
                first = None
                prev = None


if __name__ == '__main__':
    solution = Solution()
