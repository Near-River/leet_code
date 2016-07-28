#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: return head

        curr, head = head, head.next
        behind = head.next
        head.next = curr
        curr.next = behind
        front, curr = curr, behind

        count = 1
        while curr != None:
            if count % 2 != 0:
                behind = curr.next
                if behind == None: break
                curr.next = behind.next
                behind.next = curr
                front.next = behind
            else:
                front = curr
                curr = curr.next
            count += 1

        return head


if __name__ == '__main__':
    solution = Solution()
