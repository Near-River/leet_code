#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5
"""


# class ListNode(object):
def __init__(self, x):
    self.val = x
    self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head
        count = 0
        while curr != None:  # access the size of the LinkedList
            count += 1
            curr = curr.next
        curr = head

        i, idx = 0, count - n
        if idx == 0:  # remove the head from the LinkedList
            head = head.next
            return head

        while curr != None:
            i += 1
            if i == idx:
                temp = curr.next
                curr.next = temp.next
                break
            curr = curr.next

        return head


if __name__ == '__main__':
    solution = Solution()
