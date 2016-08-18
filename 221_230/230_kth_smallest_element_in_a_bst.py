#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?

Hint:
    Try to utilize the property of a BST.
    What if you could modify the BST node's structure?
    The optimal runtime complexity is O(height of BST).
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        """
                _______6______
               /              \
            ___2__          ___8__
           /      \        /      \
           1      _4       7       9
                 /  \
                 3   5
        """
        curr = root
        ret, stack = 0, [root]
        for _ in range(k):
            if curr:
                while curr.left:
                    curr = curr.left
                    stack.append(curr)
            curr = stack.pop()
            ret = curr.val
            if curr.right: stack.append(curr.right)
            curr = curr.right
        return ret


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    node1 = TreeNode(1)
    node2 = TreeNode(4)
    root.left = node1
    root.right = node2
    node1.right = TreeNode(2)
    print(solution.kthSmallest(root, 3))
