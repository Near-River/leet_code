#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None: return
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        nodes = []
        curr = head
        for i in range((length + 1) // 2):
            nodes.append(curr)
            curr = curr.next
        idx = length // 2 - 1
        (nodes[-1]).next = None
        for i in range(idx, -1, -1):
            node = nodes[i]
            nextInsert = curr.next
            curr.next = node.next
            node.next = curr
            curr = nextInsert


if __name__ == '__main__':
    solution = Solution()
