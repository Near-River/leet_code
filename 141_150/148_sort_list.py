#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sort a linked list in O(n log n) time using constant space complexity.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # solution one: Quick Sort (Time Limit Exceeded)
        if head is None or head.next is None: return head

        def quick_sort(head):
            if head.next is None: return head
            leftHead = rightHead = None
            left = right = None
            compare = head.val
            curr = head.next
            head.next = None
            while curr:
                if curr.val < compare:
                    if leftHead is None:
                        left = leftHead = curr
                    else:
                        left.next = curr
                        left = left.next
                else:
                    if rightHead is None:
                        right = rightHead = curr
                    else:
                        right.next = curr
                        right = right.next
                curr = curr.next
            if leftHead:
                left.next = None
                leftHead = quick_sort(leftHead)
            if rightHead:
                right.next = None
                rightHead = quick_sort(rightHead)
            ret = leftHead if leftHead else head
            curr = ret
            while curr.next: curr = curr.next
            if leftHead:
                curr.next = head
                curr = curr.next
            curr.next = rightHead if rightHead else None
            return ret

        # return quick_sort(head)

        # solution two: Merge Sort
        if head is None or head.next is None: return head
        curr, length = head, 0
        while curr:
            curr = curr.next
            length += 1

        def merge_sort(head, length):
            if head.next is None: return head

            prev = left = right = head
            for i in range(0, length // 2):
                prev = right
                right = right.next
            prev.next = None

            left = merge_sort(left, length // 2)
            right = merge_sort(right, length - length // 2)

            preHead = ListNode(-1)
            curr = preHead.next
            p1, p2 = left, right
            while p1 and p2:
                if p1.val < p2.val:
                    curr.next = p1
                    curr = curr.next
                    p1 = p1.next
                else:
                    curr.next = p2
                    curr = curr.next
                    p2 = p2.next
            curr.next = p1 if p1 else p2
            return preHead.next

        return merge_sort(head, length)


if __name__ == '__main__':
    solution = Solution()
