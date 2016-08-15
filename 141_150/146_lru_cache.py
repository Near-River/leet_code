#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.
"""


class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache(object):
    # HashMap + Double LinkedList
    # def __init__(self, capacity):
    #     """
    #     :type capacity: int
    #     """
    #     self.capacity = capacity
    #     self.count = 0
    #     self.list = []  # imitate the doubly linked-list
    #     self.hashmap = {}
    #
    # def get(self, key):
    #     """
    #     :rtype: int
    #     """
    #     if key not in self.list: return -1
    #     self.list.remove(key)
    #     self.list.append(key)
    #     return self.hashmap[key]
    #
    # def set(self, key, value):
    #     """
    #     :type key: int
    #     :type value: int
    #     :rtype: nothing
    #     """
    #     self.hashmap[key] = value
    #     if key not in self.list:
    #         if self.count < self.capacity:
    #             self.count += 1
    #         else:
    #             self.list.remove(self.list[0])
    #     else:
    #         self.list.remove(key)
    #     self.list.append(key)

    def __init__(self, capacity):
        self.hash = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity

    def push_back(self, node):
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.hash[self.head.next.key] = self.head

    def kick(self, prev):
        # change "prev->node->next->...->tail"  to "prev->next->...->tail->node"
        node = prev.next
        if node == self.tail: return
        prev.next = node.next
        if prev.next is not None: self.hash[prev.next.key] = prev
        node.next = None
        self.push_back(node)

    def get(self, key):
        if key not in self.hash: return -1
        self.kick(self.hash[key])
        return self.hash[key].next.value

    def set(self, key, value):
        if key in self.hash:
            self.kick(self.hash[key])
            self.hash[key].next.value = value
        else:
            self.push_back(LinkedNode(key, value))
            if len(self.hash) > self.capacity:
                self.pop_front()


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.set(2, 1)
    cache.set(1, 1)
    cache.set(2, 3)
    cache.set(4, 1)
    print(cache.get(1))
    print(cache.get(2))
