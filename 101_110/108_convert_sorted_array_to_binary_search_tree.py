#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        left = self.sortedArrayToBST(nums[:mid])
        right = self.sortedArrayToBST(nums[mid + 1:])
        root.left = left
        root.right = right
        return root


if __name__ == '__main__':
    solution = Solution()
