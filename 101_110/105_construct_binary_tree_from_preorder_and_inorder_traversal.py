#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # solution one: recursion: Memory Limit Exceeded
        if not preorder: return None
        num = preorder[0]
        root = TreeNode(num)
        idx = inorder.index(num)
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        # return root

        # solution two
        def helper(preorder, s0, e0, inorder, s1, e1):
            if s0 > e0 or s1 > e1: return None
            num = preorder[s0]
            root = TreeNode(num)
            idx = self.map.get(num)
            left = helper(preorder, s0 + 1, s0 + idx - s1, inorder, s1, idx - 1)
            right = helper(preorder, s0 + 1 + idx - s1, e0, inorder, idx + 1, e1)
            root.left = left
            root.right = right
            return root

        if not preorder: return None
        # consider to use HashMap to store the value's location in inorder list
        self.map = {}
        for i in range(len(inorder)): self.map[inorder[i]] = i

        return helper(preorder=preorder, s0=0, e0=len(preorder) - 1, inorder=inorder, s1=0, e1=len(inorder) - 1)


if __name__ == '__main__':
    solution = Solution()
