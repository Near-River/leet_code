#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # solution one
        number_lst1, number_lst2 = [], []
        while l1 != None:
            number_lst1.append(str(l1.val))
            l1 = l1.next
        while l2 != None:
            number_lst2.append(str(l2.val))
            l2 = l2.next
        number = int((''.join(number_lst1))[::-1]) + int((''.join(number_lst2))[::-1])
        s_number = str(number)[::-1]

        i, l3 = 0, ListNode(0)
        res = l3
        while i < len(s_number):
            l3.val = s_number[i]
            l3.next = ListNode(0)
            l3 = l3.next
            i += 1
        l3 = None

        # solution two
        carry, l3 = 0, ListNode(0)
        res = l3
        while l1 != None or l2 != None:
            p = l1.val if l1 != None else 0
            q = l2.val if l2 != None else 0
            number = (p + q) % 10
            l3.val = carry + number
            carry = (p + q) // 10
            l3.next = ListNode(0)
            l3 = l3.next

            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        l3 = None

        return res
