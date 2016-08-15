#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

You should return [1, 3, 4].
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        ret = []
        queue = deque([root])
        while queue:
            temp = []
            ret.append(queue[-1].val)
            while queue:
                node = queue.popleft()
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            queue.extend(temp)
        return ret


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(-2)
    node1 = TreeNode(1)
    node2 = TreeNode(3)
    node3 = TreeNode(5)
    root.left = node1
    root.right = node2
    node1.right = node3
    print(solution.rightSideView(root))