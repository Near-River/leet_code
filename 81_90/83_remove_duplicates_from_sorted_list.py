#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # solution one
        preHead = ListNode(-1)
        preHead.next = head
        prev, curr = preHead, head
        if head is not None:
            prev = curr
            curr = curr.next
        while curr is not None:
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        # return preHead.next

        # solution two
        curr = head
        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


if __name__ == '__main__':
    solution = Solution()
