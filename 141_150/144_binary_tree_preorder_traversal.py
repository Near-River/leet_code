#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        stack = [root]
        ret = []
        while stack:
            node = stack.pop()
            ret.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)

        return ret

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(-2)
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    root.left = node1
    node1.right = node2
    print(solution.preorderTraversal(root))
