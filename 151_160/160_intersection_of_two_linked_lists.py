#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3

begin to intersect at node c1.
Notes:
    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # solution one
        if headA is None or headB is None: return None
        prevA, prevB = ListNode(-1), ListNode(-1)
        prevA.next = headA
        prevB.next = headB
        p1, p2 = prevA, prevB
        lenA, lenB = 0, 0
        while p1.next and p2.next:
            p1 = p1.next
            p2 = p2.next
            lenA += 1
        lenB = lenA
        if p1.next is None:
            while p2:
                if p2 == p1: break
                p2 = p2.next
                lenB += 1
            if p2 is None: return None
            p1, p2 = prevA, prevB
            for i in range(lenB - lenA): p2 = p2.next
        else:
            while p1:
                if p1 == p2: break
                p1 = p1.next
                lenB += 1
            if p1 is None: return None
            p1, p2 = prevA, prevB
            for i in range(lenB - lenA): p1 = p1.next
        while p1 and p2:
            if p1 == p2: return p1
            p1 = p1.next
            p2 = p2.next

        # solution two
        if headA is None or headB is None: return None
        prevA, prevB = ListNode(-1), ListNode(-1)
        prevA.next = headA
        prevB.next = headB
        p1, p2 = prevA, prevB
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
        if p1 is None:
            p1 = prevB
            while p2:
                p2 = p2.next
                p1 = p1.next
            p2 = prevA
        else:
            p2 = prevA
            while p1:
                p1 = p1.next
                p2 = p2.next
            p1 = prevB
        while p1 and p2:
            if p1 == p2: return p1
            p1 = p1.next
            p2 = p2.next
        return None


if __name__ == '__main__':
    solution = Solution()
