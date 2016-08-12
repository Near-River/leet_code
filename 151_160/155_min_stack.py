#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._sort = []

    def _add(self, x):
        if not self._sort:
            self._sort.append(x)
        else:
            s, e = 0, len(self._sort) - 1
            while s <= e:
                if s == e:
                    if x > self._sort[s]:
                        self._sort.insert(s + 1, x)
                    else:
                        self._sort.insert(s, x)
                    break
                mid = (s + e) // 2
                if x > self._sort[mid]:
                    s = mid + 1
                else:
                    e = mid

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._stack.append(x)
        self._add(x)

    def pop(self):
        """
        :rtype: void
        """
        element = self._stack.pop()
        self._sort.remove(element)

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._sort[0]


if __name__ == '__main__':
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.getMin())
    stack.pop()
    print(stack.top())
    print(stack.getMin())
