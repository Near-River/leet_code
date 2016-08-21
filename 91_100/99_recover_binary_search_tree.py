#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None: return
        curr, stack = root, [root]
        first = second = None
        _next = None
        flag = False
        while stack:
            if curr:
                while curr.left:
                    curr = curr.left
                    stack.append(curr)
            node = curr = stack.pop()
            if first is None:
                first = node
            elif second is None:
                if first.val > node.val:
                    second = _next = node
                else:
                    first = node
            else:
                if second.val > node.val:
                    second, flag = node, True
                    break
                else:
                    second = node
            if curr.right: stack.append(curr.right)
            curr = curr.right

        if not flag: second = _next
        first.val, second.val = second.val, first.val


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.left = node1
    root.right = node2
    print(solution.recoverTree(root))
