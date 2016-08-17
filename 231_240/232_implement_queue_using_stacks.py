#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement the following operations of a queue using stacks.
    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

Notes:
    You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is
    empty operations are valid.
    Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque
    (double-ended queue), as long as you use only standard operations of a stack.
    You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""


class Queue(object):
    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.stack = []
    #
    # def push(self, x):
    #     """
    #     :type x: int
    #     :rtype: nothing
    #     """
    #     _stack, _len = [], len(self.stack)
    #     for _ in range(_len): _stack.append(self.stack.pop())
    #     _stack.append(x)
    #     for _ in range(_len + 1): self.stack.append(_stack.pop())
    #
    # def pop(self):
    #     """
    #     :rtype: nothing
    #     """
    #     self.stack.pop()
    #
    # def peek(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.stack[-1]
    #
    # def empty(self):
    #     """
    #     :rtype: bool
    #     """
    #     return len(self.stack) == 0

    # Amortized Stack
    def __init__(self):
        self.front = None
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        if len(self.stack1) == 0: self.front = x
        self.stack1.append(x)

    def pop(self):
        if len(self.stack2) == 0:
            _len = len(self.stack1)
            for _ in range(_len): self.stack2.append(self.stack1.pop())
        self.stack2.pop()

    def peek(self):
        if len(self.stack2) > 0: return self.stack2[-1]
        return self.front

    def empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0


if __name__ == '__main__':
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.peek())
