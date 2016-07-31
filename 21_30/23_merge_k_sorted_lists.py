#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

import heapq


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        # Tags: Divide and Conquer(分而治之) & Linked List & Heap

        # solution one
        # head, length = None, len(lists)
        #
        # def is_empty_lists():
        #     for lst in lists:
        #         if lst != None: return False
        #     return True
        #
        # def get_minimum_value():
        #     """
        #     :return: the minimum value of all the ListNode's val in the lists
        #     """
        #     vals, idxs = [], []
        #     for i in range(length):
        #         if lists[i] != None:
        #             vals.append((lists[i]).val)
        #             idxs.append(i)
        #     _min = min(vals)
        #     _idx = idxs[vals.index(_min)]
        #     lists[_idx] = lists[_idx].next
        #     return _min
        #
        # if is_empty_lists(): return None
        # prev = curr = head = ListNode(0)
        # while not is_empty_lists():
        #     curr.val = get_minimum_value()
        #     curr.next = ListNode(0)
        #     prev, curr = curr, curr.next
        # prev.next = None
        # return head

        # solution two: Divide and Conquer + Merge sort
        def merge2lists(l1, l2):
            """
            :param l1: ListNode
            :param l2: ListNode
            :return: ListNode type
            """
            if l1 is None: return l2
            if l2 is None: return l1
            prev = curr = head = ListNode(0)
            while l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    curr.val = l1.val
                    l1 = l1.next
                else:
                    curr.val = l2.val
                    l2 = l2.next
                curr.next = ListNode(0)
                prev, curr = curr, curr.next
            prev.next = l1 if l1 is not None else l2
            return head

        def mergeKlists(lists):
            length = len(lists)
            if length == 1: return lists[0]
            if length == 2: return merge2lists(lists[0], lists[1])
            mid = (length - 1) // 2
            return merge2lists(mergeKlists(lists[:mid]), mergeKlists(lists[mid:]))

        if lists == []: return None
        # return mergeKlists(lists)

        # solution three: Heap(Priority Queue)
        heap = []
        heapq.heapify(heap)  # turn list to heap
        for lst in lists:
            if lst == None: continue
            while lst != None:
                heapq.heappush(heap, lst.val)
                lst = lst.next

        if heap == []: return None
        prev = curr = head = ListNode(0)
        for i in range(len(heap)):
            curr.val = heapq.heappop(heap)
            curr.next = ListNode(0)
            prev, curr = curr, curr.next
        prev.next = None
        return head


if __name__ == '__main__':
    solution = Solution()
    print(solution.mergeKLists([]))
