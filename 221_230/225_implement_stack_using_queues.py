#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement the following operations of a stack using queues.
    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    empty() -- Return whether the stack is empty.

Notes:
    You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size,
    and is empty operations are valid.
    Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque
    (double-ended queue), as long as you use only standard operations of a queue.
    You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""

from collections import deque


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._top = None
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self._top = x
        self.queue.append(x)
        _len = len(self.queue)
        for _ in range(_len - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.popleft()
        if not self.empty(): self._top = self.queue[0]

    def top(self):
        """
        :rtype: int
        """
        return self._top

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0


if __name__ == '__main__':
    stack = Stack()
