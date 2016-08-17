#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the
lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5

For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since
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

        def search_node(root, path, target):
            if root.val == target:
                return
            elif root.val < target:
                path.append(root.right)
                search_node(root.right, path, target)
            else:
                path.append(root.left)
                search_node(root.left, path, target)

        if root is None: return None
        path1, path2 = [root], [root]
        search_node(root, path1, p.val)
        search_node(root, path2, q.val)
        i = 0
        while i < min(len(path1), len(path2)):
            if path1[i].val != path2[i].val: return path1[i - 1]
            i += 1
        return path1[i - 1]


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(6)
    node1 = TreeNode(2)
    node2 = TreeNode(8)
    node3 = TreeNode(0)
    root.left = node1
    root.right = node2
    node1.left = node3
    print(solution.lowestCommonAncestor(root, node3, node1))
