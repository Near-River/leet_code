#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s)
from beginWord to endWord, such that:
    Only one letter can be changed at a time
    Each intermediate word must exist in the word list

For example,
Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
"""
from collections import deque


class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """

        # solution one: Time Limit Exceeded
        wordLen = len(beginWord)
        wordlist.add(beginWord)
        wordlist.add(endWord)
        currQueue = deque([(beginWord, 1, [beginWord])])
        ret, ladderLen = [], -1

        while currQueue:
            nextQueue = deque()
            while currQueue:
                beginWord, count, transform = currQueue.popleft()
                if beginWord == endWord:
                    if ladderLen == -1:
                        ladderLen = count
                    elif count > ladderLen:
                        return ret
                    ret.append(transform)
                if beginWord in wordlist: wordlist.remove(beginWord)
                for i in range(wordLen):
                    leftPart, rightPart = beginWord[:i], beginWord[i + 1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if beginWord[i] != c:
                            s = leftPart + c + rightPart
                            if s in wordlist: nextQueue.append((s, count + 1, transform + [s]))
            currQueue = nextQueue

        # return ret

        # solution two
        def buildPath(path, word):
            path.append(word)
            if not prevMap[word]:  # word is beginWord
                ret.append(path[::-1])
            else:
                for prevWord in prevMap[word]: buildPath(path, prevWord)
            path.pop()

        wordLen = len(beginWord)
        ret = []
        wordlist.add(beginWord)
        wordlist.add(endWord)
        prevMap = {}  # store the previous words which can transform to the target(next) word
        for word in wordlist: prevMap[word] = []
        candidates = [set(), set()]
        candidates[0].add(beginWord)
        current, previous = 0, 1
        while True:
            current, previous = previous, current
            for word in candidates[previous]: wordlist.remove(word)
            candidates[current].clear()
            for word in candidates[previous]:
                for i in range(wordLen):
                    leftPart, rightPart = word[:i], word[i + 1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != c:
                            nextWord = leftPart + c + rightPart
                            if nextWord in wordlist:
                                candidates[current].add(nextWord)
                                prevMap[nextWord].append(word)
            if len(candidates[current]) == 0: return []
            if endWord in candidates[current]: break

        buildPath([], endWord)  # 路径反追踪
        return ret


if __name__ == '__main__':
    solution = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordlist = {"hot", "dot", "dog", "lot", "log"}
    print(solution.findLadders(beginWord, endWord, wordlist))
    print(solution.findLadders('a', 'c', {'a', 'b', 'c'}))
    print(solution.findLadders('hot', 'dog', {'hot', 'dog'}))
    print(solution.findLadders('hot', 'dog', {'hot', 'dog', 'dot'}))
    print(solution.findLadders('lost', 'miss', {"most", "mist", "miss", "lost", "fist", "fish"}))
    beginWord = "qa"
    endWord = "sq"
    wordlist = {"si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar",
                "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma",
                "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge",
                "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh",
                "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be",
                "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"}
    print(solution.findLadders(beginWord, endWord, wordlist))
