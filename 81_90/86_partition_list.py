#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        preHead = ListNode(-1)
        preHead.next = head
        prev, begin = preHead, head
        while begin is not None:
            if begin.val < x:
                prev = begin
                begin = begin.next
            else:
                front, curr = prev, begin
                while curr is not None:
                    while curr is not None and curr.val >= x:
                        front = curr
                        curr = curr.next
                    if curr is not None:
                        front.next = curr.next
                        curr.next = begin
                        prev.next = curr
                        prev = curr
                        curr = front.next
                return preHead.next

        return preHead.next


if __name__ == '__main__':
    solution = Solution()
