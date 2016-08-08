#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        def helper(postorder, s0, e0, inorder, s1, e1):
            if s0 > e0 or s1 > e1: return None
            num = postorder[e0]
            root = TreeNode(num)
            idx = self.map.get(num)

            left = helper(postorder, s0, s0 + idx - s1 - 1, inorder, s1, idx - 1)
            right = helper(postorder, s0 + idx - s1, e0 - 1, inorder, idx + 1, e1)

            root.left = left
            root.right = right
            return root

        if not postorder: return None
        # consider to use HashMap to store the value's location in inorder list
        self.map = {}
        for i in range(len(inorder)): self.map[inorder[i]] = i

        return helper(postorder=postorder, s0=0, e0=len(postorder) - 1, inorder=inorder, s1=0, e1=len(inorder) - 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.buildTree([1, 2], [1, 2]))
