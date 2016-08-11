#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:
    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?
"""


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # solution one: Wrong(the same rating children can get different candy,
        #                       corresponding to the qestion: high rating correspond to more candy)
        # length = len(ratings)
        # if length < 2: return length
        # ret, i = 0, 0
        # while i < length:
        #     if i + 1 < length and ratings[i] >= ratings[i + 1]:
        #         allCandy, candy = 1, 1
        #         j = i + 1
        #         while j < length and ratings[j - 1] >= ratings[j]:
        #             candy = candy if ratings[j] == ratings[j - 1] else candy - 1
        #             allCandy += candy
        #             j += 1
        #         ret += (allCandy + (j - i) * (1 - candy))
        #         if j == length: return ret
        #         ret -= 1
        #         i = j - 1  # location to the valley
        #     else:
        #         j = i + 1
        #         allCandy, candy = 1, 1
        #         while j < length and ratings[j - 1] <= ratings[j]:
        #             candy = candy if ratings[j] == ratings[j - 1] else candy + 1
        #             allCandy += candy
        #             j += 1
        #         if j == length: return ret + allCandy
        #         k, j = j, j - 1
        #         topCandy = candy
        #         allCandy2 = 0
        #         while k < length and ratings[k - 1] >= ratings[k]:
        #             candy = candy if ratings[k] == ratings[k - 1] else candy - 1
        #             allCandy2 += candy
        #             k += 1
        #         if candy > 1:
        #             allCandy2 -= (k - j - 1) * (candy - 1)
        #         elif candy < 1:
        #             count = 1
        #             while ratings[j] == ratings[j - 1]:
        #                 j -= 1
        #                 count += 1
        #             allCandy2 += (k - j) * (1 - candy)
        #             allCandy -= count * topCandy
        #         ret += allCandy + allCandy2
        #         if k == length: return ret
        #         ret -= 1
        #         i = k - 1  # location to the valley
        #
        # return ret

        # solution two
        length = len(ratings)
        if length < 2: return length
        candy = [1] * length
        i = 0
        while i < length - 1:
            if ratings[i + 1] > ratings[i]: candy[i + 1] = candy[i] + 1
            i += 1
        while i >= 1:
            if ratings[i - 1] > ratings[i] and candy[i - 1] <= candy[i]: candy[i - 1] = candy[i] + 1
            i -= 1
        return sum(candy)


if __name__ == '__main__':
    solution = Solution()
    print(solution.candy([5, 4, 4, 3, 1, 2]))
    print(solution.candy([5, 4, 4, 3, 1, 2, 3, 4, 4]))
    print(solution.candy([3, 3, 1, 3, 5, 9, 9, 9, 6, 6, 5, 3, 1]))
    print(solution.candy([4, 2, 3, 2, 1]))
