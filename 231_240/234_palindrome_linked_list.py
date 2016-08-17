#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a singly linked list, determine if it is a palindrome.

Follow up: Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None: return True
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        mid = length // 2 if length % 2 == 0 else length // 2 + 1
        left = right = head
        for _ in range(mid - 1): right = right.next
        prev = right
        curr = right.next
        while curr.next:
            node = curr.next
            curr.next = node.next
            node.next = prev.next
            prev.next = node
        right = prev.next
        for _ in range(length // 2):
            if left.val != right.val: return False
            left = left.next
            right = right.next
        return True


if __name__ == '__main__':
    solution = Solution()
