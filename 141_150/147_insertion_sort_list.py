#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sort a linked list using insertion sort.

插入排序都采用in-place在数组上实现。具体算法描述如下：
1 从第一个元素开始，该元素可以认为已经被排序
2 取出下一个元素，在已经排序的元素序列中从后向前扫描
3 如果该元素（已排序）大于新元素，将该元素移到下一位置
4 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5 将新元素插入到该位置后
6 重复步骤2~5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head is None or head.next is None: return head
        # left = head.next
        # tail = head
        # head.next = None
        # while left:
        #     insert = left
        #     left = left.next
        #     insert.next = None
        #     if insert.val <= head.val:
        #         insert.next = head
        #         head = insert
        #     elif tail.val <= insert.val:
        #         tail.next = insert
        #         tail = tail.next
        #     else:
        #         curr = head
        #         while curr.next and curr.next.val < insert.val:
        #             curr = curr.next
        #         insert.next = curr.next
        #         curr.next = insert
        # return head

        # optimization
        if head is None or head.next is None: return head
        left = head.next
        preHead = ListNode(-1)
        preHead.next = tail = head
        head.next = None
        while left:
            insert = left
            left = left.next
            insert.next = None
            if tail.val <= insert.val:
                tail.next = insert
                tail = tail.next
            else:
                curr = preHead
                while curr.next and curr.next.val < insert.val: curr = curr.next
                insert.next = curr.next
                curr.next = insert

        return preHead.next


if __name__ == '__main__':
    solution = Solution()
    a, b, c = ListNode(3), ListNode(2), ListNode(4)
    a.next = b
    b.next = c
    h = solution.insertionSortList(a)
