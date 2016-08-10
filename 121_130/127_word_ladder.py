#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence
from beginWord to endWord, such that:
    Only one letter can be changed at a time
    Each intermediate word must exist in the word list

For example,
Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
"""
from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        """
        转化过程(类似于图论中求最短路径问题)：
        1. 将每个单词看成图的一个节点。
        2. 当单词s1改变一个字符可以变成存在于字典的单词s2时，则s1与s2之间有连接。
        3. 给定s1和s2，问题转化成了求在图中从s1->s2的最短路径长度。

        无论是求最短路径长度还是求所有最短路径，都是用BFS。在BFS中有三个关键步骤需要实现:
        1. 如何找到与当前节点相邻的所有节点。
            这里可以有两个策略：
            (1) 遍历整个字典，将其中每个单词与当前单词比较，判断是否只差一个字符。
            复杂度为：n*w，n为字典中的单词数量，w为单词长度。
            (2) 遍历当前单词的每个字符x，将其改变成a~z中除x外的任意一个，形成一个新的单词，在字典中判断是否存在。
            复杂度为：26*w，w为单词长度。
        2. 如何标记一个节点已经被访问过，以避免重复访问。 可以将访问过的单词从字典中删除。
        3. 一旦BFS找到目标单词，如何backtracking找回路径？
        """
        wordList.add(endWord)
        length = len(beginWord)
        queue = deque()
        queue.append((beginWord, 1))
        while queue:
            beginWord, transform = queue.popleft()
            if beginWord == endWord: return transform
            for i in range(length):
                leftPart, rightPart = beginWord[:i], beginWord[i + 1:]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if beginWord[i] != c:
                        s = leftPart + c + rightPart
                        if s in wordList:
                            queue.append((s, transform + 1))
                            wordList.remove(s)
        return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.ladderLength('a', 'c', {'a', 'b', 'c'}))
    print(solution.ladderLength('hot', 'dog', {'hot', 'dog'}))
    print(solution.ladderLength('hot', 'dog', {'hot', 'dog', 'dot'}))
    print(solution.ladderLength('lost', 'miss', {"most", "mist", "miss", "lost", "fist", "fish"}))
    beginWord = "qa"
    endWord = "sq"
    wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar",
                "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma",
                "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge",
                "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh",
                "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be",
                "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]
    print(solution.ladderLength(beginWord, endWord, set(wordList)))
