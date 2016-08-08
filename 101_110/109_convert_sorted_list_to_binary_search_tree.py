#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None: return None

        def helper(nums, start, end):
            if end < start: return None
            mid = (end + start) // 2
            root = TreeNode(nums[mid])
            left = helper(nums, start, mid - 1)
            right = helper(nums, mid + 1, end)
            root.left = left
            root.right = right
            return root

        length, array = 0, []
        curr = head
        while curr is not None:
            array.append(curr.val)
            curr = curr.next
            length += 1
        return helper(array, 0, length - 1)


if __name__ == '__main__':
    solution = Solution()
