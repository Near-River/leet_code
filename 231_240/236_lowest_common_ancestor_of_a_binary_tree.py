#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as
the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since
a node can be a descendant of itself according to the LCA definition.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # solution one: Recursion
        if root is None: return None
        if root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        # return left if left else right

        # solution two
        def search_path(root, target):
            stack = []
            lastVisit = None
            while stack or root:
                if root:
                    stack.append(root)
                    root = root.left
                else:
                    peek = stack[-1]
                    if peek == target: return stack
                    if peek.right and lastVisit != peek.right:
                        root = peek.right
                    else:
                        lastVisit = stack.pop()
                        root = None
            return stack

        if root is None: return None
        path1 = search_path(root, p)
        path2 = search_path(root, q)
        k = 0
        while k < min(len(path1), len(path2)):
            if path1[k].val != path2[k].val: return path1[k - 1]
            k += 1
        return path1[k - 1]


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    root.left = node1
    root.right = node2
    node1.right = node3
    print(solution.lowestCommonAncestor(root, node3, node2))
