#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,
return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        preHead = ListNode(-1)
        preHead.next = head
        prev = preHead
        for i in range(m - 1): prev = prev.next
        start = prev.next
        for i in range(n - m):
            curr = start.next
            start.next = curr.next
            curr.next = prev.next
            prev.next = curr

        return preHead.next


if __name__ == '__main__':
    solution = Solution()
