#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a complete binary tree, count the number of nodes.
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level
are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        ret, depth = 0, 0
        curr = root
        while curr.left:
            curr = curr.left
            ret += (1 << depth)
            depth += 1
        if depth == 0: return 1

        def helper(h, start, end):
            mid = (start + end) // 2
            curr = root
            temp = 1 << (h - 1)
            for i in range(h):
                curr = curr.left if mid & temp == 0 else curr.right
                temp >>= 1
            if curr is None:
                if start + 1 >= end: return start
                return helper(h, start, mid - 1)
            else:
                if start == end: return start + 1
                return helper(h, mid + 1, end)

        return ret + helper(depth, 0, (1 << depth) - 1)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(2)
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    root.left = node1
    root.right = node2
    node1.left = TreeNode(5)
    print(solution.countNodes(root))
