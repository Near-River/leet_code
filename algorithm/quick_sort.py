#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
快速排序
"""


def quick_sort(nums, low, high):
    if low >= high: return
    i, j = low, high
    pivot = nums[i]
    while i < j:
        while i < j and nums[j] >= pivot: j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= pivot: i += 1
        nums[j] = nums[i]
    nums[i] = pivot
    quick_sort(nums, low, i - 1)
    quick_sort(nums, i + 1, high)
    return nums


if __name__ == '__main__':
    lst = [32, 12, 3, 21, 43, 102, 44, 1]
    new_lst = quick_sort(lst, 0, len(lst) - 1)
    print(new_lst)
