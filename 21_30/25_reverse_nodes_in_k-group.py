#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # solution one
        # if k <= 1: return head
        # curr, length = head, 0
        # while curr != None:
        #     curr = curr.next
        #     length += 1
        # if length < k: return head
        #
        # first = tail = head
        # prev = behind = head
        # for i in range(1, k):
        #     for j in range(k - i):
        #         tail = tail.next
        #     if i == 1:
        #         behind = tail.next
        #         prev = head = tail
        #         tail.next = first
        #         tail = first
        #     else:
        #         tail.next = first
        #         prev.next = tail
        #         prev, tail = tail, first
        # first.next = behind
        # prev = first
        # first = tail = behind
        # carry = (length - k) // k
        # for c in range(carry):
        #     # reverse the left nodes in k-group
        #     for i in range(1, k):
        #         for j in range(k - i):
        #             tail = tail.next
        #         if i == 1: behind = tail.next
        #         tail.next = first
        #         prev.next = tail
        #         prev, tail = tail, first
        #     first.next = behind
        #     prev = first
        #     first = tail = behind
        #
        # return head

        # solution two: insert an pre-head node
        if k == 1: return head
        curr, length = head, 0
        while curr != None:  # get the LinkedList size
            curr = curr.next
            length += 1
        if length < k: return head

        preHead = ListNode(-1)
        preHead.next = head
        pre, curr = preHead, head
        carry = length // k
        for c in range(carry):
            for i in range(k - 1):
                temp = curr.next
                curr.next = temp.next
                temp.next = pre.next
                pre.next = temp
            pre, curr = curr, curr.next

        return preHead.next


if __name__ == '__main__':
    solution = Solution()
    curr = l1 = ListNode(1)
    for i in range(3):
        curr.next = ListNode(i + 2)
        curr = curr.next

    l2 = solution.reverseKGroup(l1, 2)
    while l2 is not None:
        print(l2.val)
        l2 = l2.next
