#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3

return [1, 3, 2].

Note: Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # solution one: recursion
        if root is None: return []
        ret = []
        if root.left: ret.extend(self.inorderTraversal(root.left))
        ret.append(root.val)
        if root.right: ret.extend(self.inorderTraversal(root.right))
        # return ret

        # solution two: iteration
        if root is None: return []
        ret, stack = [], []
        stack.append(root)
        while stack:
            curr = stack[-1]
            if curr.left:
                stack.append(curr.left)
                curr.left = None
            else:
                ret.append(curr.val)
                stack.pop()
                if curr.right: stack.append(curr.right)

        return ret


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.left = None
    root.right = node1
    node1.left = node2
    node1.right = None
    node2.left = None
    node2.right = None

    print(solution.inorderTraversal(root))
