#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prevHead = ListNode(-1)
        prevHead.next = head
        curr = prevHead
        while curr:
            while curr.next and curr.next.val != val:
                curr = curr.next
            if curr.next is None: return prevHead.next
            curr.next = curr.next.next
        return prevHead.next


if __name__ == '__main__':
    solution = Solution()
