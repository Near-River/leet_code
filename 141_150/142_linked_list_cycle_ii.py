#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Note: Do not modify the linked list.

Follow up: Can you solve it without using extra space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        p1 = p2 = head
        while p2 is not None:
            p1 = p1.next
            if p2.next is None: return None
            p2 = p2.next.next
            if p2 == p1:
                p1 = head
                while True:
                    if p1 == p2: return p1
                    p1 = p1.next
                    p2 = p2.next
        return None


if __name__ == '__main__':
    solution = Solution()
