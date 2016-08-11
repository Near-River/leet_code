#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a linked list, determine if it has a cycle in it.

Follow up: Can you solve it without using extra space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: return False
        p1 = p2 = head
        while p2 is not None:
            if p2.next == p1: return True
            p1 = p1.next
            if p2.next is None: return False
            p2 = p2.next.next
        return False


if __name__ == '__main__':
    solution = Solution()
