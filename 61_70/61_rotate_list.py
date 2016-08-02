#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        prev = curr = head
        length = 0
        while curr is not None:
            length += 1
            prev = curr
            curr = curr.next
        if length == 0 or k % length == 0: return head
        k = k % length
        tail = prev  # locate the tail pointer
        curr = head
        for i in range(length - k - 1): curr = curr.next
        tail.next = head
        head = curr.next
        curr.next = None

        return head


if __name__ == '__main__':
    solution = Solution()
