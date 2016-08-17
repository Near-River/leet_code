#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Reverse a singly linked list.

Hint: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return head
        prev = head
        while head.next:
            curr = head.next
            head.next = curr.next
            curr.next = prev
            prev = curr
        return prev


if __name__ == '__main__':
    solution = Solution()
