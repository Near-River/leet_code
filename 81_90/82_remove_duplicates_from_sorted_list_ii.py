#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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
        if head is None: return head
        preHead = ListNode(-1)
        preHead.next = head
        prev = preHead
        start, end = head, head.next

        while end is not None:
            if start.val != end.val:
                prev = start
                start = end
                end = end.next
            else:
                while end.next is not None and end.next.val == start.val:
                    end = end.next
                behind = end.next
                prev.next = behind
                if behind is None: break
                start = behind
                end = behind.next

        return preHead.next


if __name__ == '__main__':
    solution = Solution()
