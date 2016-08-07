#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        nums = [i for i in range(1, n + 1)]

        def buildBFS(nums):
            if not nums: return []
            if len(nums) == 1: return [TreeNode(nums[0])]
            ret = []
            for i in range(len(nums)):
                num = nums[i]
                leftSubTrees = buildBFS(nums[:i])
                rightSubTrees = buildBFS(nums[i + 1:])
                if leftSubTrees != [] and rightSubTrees != []:
                    for node1 in leftSubTrees:
                        for node2 in rightSubTrees:
                            root = TreeNode(num)
                            root.left = node1
                            root.right = node2
                            ret.append(root)
                else:
                    if not leftSubTrees:
                        for node in rightSubTrees:
                            root = TreeNode(num)
                            root.right = node
                            ret.append(root)
                    else:
                        for node in leftSubTrees:
                            root = TreeNode(num)
                            root.left = node
                            ret.append(root)
            return ret

        return buildBFS(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateTrees(3))
    print(solution.generateTrees(5))
