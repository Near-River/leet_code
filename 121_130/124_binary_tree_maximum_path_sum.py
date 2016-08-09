#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree
along the parent-child connections. The path does not need to go through the root.

For example:
Given the below binary tree,
       1
      / \
     2   3
Return 6.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        There should be four ways existing for max path:
        1. Node only
        2. L-sub + Node
        3. R-sub + Node
        4. L-sub + Node + R-sub
        """
        if root is None: return 0
        self._maxPathSum = -2147483648

        def getMaxRootPathSum(root):
            """
            find the maximum pathSum through the root TreeNode
            """
            if root is None: return 0
            leftSum = max(getMaxRootPathSum(root.left), 0)
            rightSum = max(getMaxRootPathSum(root.right), 0)
            self._maxPathSum = max(self._maxPathSum, leftSum + rightSum + root.val)
            return max(root.val + leftSum, root.val + rightSum)

        _maxSum = getMaxRootPathSum(root)
        return max(self._maxPathSum, _maxSum)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(-2)
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    root.left = node1
    root.right = node2
    print(solution.maxPathSum(root))
