#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None: return None
        root = RandomListNode(head.label)
        map = {head: root}

        curr = head.next
        while curr:
            node = RandomListNode(curr.label)
            root.next = node
            map[curr] = node
            curr = curr.next
            root = root.next
        curr = head
        while curr:
            if curr.random:
                node = map[curr]
                node.random = map[curr.random]
            curr = curr.next

        return map[head]


if __name__ == '__main__':
    solution = Solution()
