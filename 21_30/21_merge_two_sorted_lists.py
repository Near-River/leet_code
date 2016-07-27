#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None: return None
        curr = l3 = ListNode(0)
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                curr.val = l1.val
                l1 = l1.next
            else:
                curr.val = l2.val
                l2 = l2.next
            curr.next = ListNode(0)
            curr = curr.next
        l_temp = l1 if l2 is None else l2
        while l_temp != None:
            curr.val = l_temp.val
            l_temp = l_temp.next
            if l_temp != None:
                curr.next = ListNode(0)
                curr = curr.next
            else:
                curr.next = None
        return l3


if __name__ == '__main__':
    solution = Solution()
