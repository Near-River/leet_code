#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
合并排序
"""

from collections import deque


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        # left and right both are sorted list
        merged, left, right = deque(), deque(left), deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())
        merged.extend(right if right else left)
        return list(merged)

    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)


if __name__ == '__main__':
    lst = [32, 12, 3, 21, 43, 102, 44, 1]
    new_lst = merge_sort(lst)
    print(new_lst)
