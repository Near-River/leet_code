#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].

Note: You may assume that all inputs are consist of lowercase letters a-z.
You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of
data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie?
"""


class TrieNode(object):
    def __init__(self):
        self.isKey = False
        self.childrens = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch in curr.childrens:
                curr = curr.childrens[ch]
            else:
                node = TrieNode()
                curr.childrens[ch] = node
                curr = node
        curr.isKey = True

    def front(self):
        return self.root


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        def search_word(root, loc, word):
            if root.isKey: self.ret.add(word)
            r, c = loc
            for k in range(4):
                i = r + self.DIRECT_X[k]
                j = c + self.DIRECT_Y[k]
                if 0 <= i < m and 0 <= j < n and board[i][j] != '#':
                    s = board[i][j]
                    if s in root.childrens:
                        board[i][j] = '#'
                        search_word(root.childrens[s], (i, j), word + s)
                        board[i][j] = s

        if len(board) == 0: return []
        m, n = len(board), len(board[0])
        trie = Trie()
        for word in words: trie.insert(word)
        root = trie.front()

        self.DIRECT_X = [1, 0, 0, -1]
        self.DIRECT_Y = [0, 1, -1, 0]
        self.ret = set()

        for i in range(m):
            for j in range(n):
                s = board[i][j]
                if s in root.childrens:
                    board[i][j] = '#'
                    search_word(root.childrens[s], (i, j), s)
                    board[i][j] = s
        return list(self.ret)


if __name__ == '__main__':
    solution = Solution()
    words = ["oath", "pea", "eat", "rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    print(solution.findWords(board, words))
    lst = ["bbaabaabaaaaabaababaaaaababb", "aabbaaabaaabaabaaaaaabbaaaba", "babaababbbbbbbaabaababaabaaa",
           "bbbaaabaabbaaababababbbbbaaa", "babbabbbbaabbabaaaaaabbbaaab", "bbbababbbbbbbababbabbbbbabaa",
           "babababbababaabbbbabbbbabbba", "abbbbbbaabaaabaaababaabbabba", "aabaabababbbbbbababbbababbaa",
           "aabbbbabbaababaaaabababbaaba", "ababaababaaabbabbaabbaabbaba", "abaabbbaaaaababbbaaaaabbbaab",
           "aabbabaabaabbabababaaabbbaab", "baaabaaaabbabaaabaabababaaaa", "aaabbabaaaababbabbaabbaabbaa",
           "aaabaaaaabaabbabaabbbbaabaaa", "abbaabbaaaabbaababababbaabbb", "baabaababbbbaaaabaaabbababbb",
           "aabaababbaababbaaabaabababab", "abbaaabbaabaabaabbbbaabbbbbb", "aaababaabbaaabbbaaabbabbabab",
           "bbababbbabbbbabbbbabbbbbabaa", "abbbaabbbaaababbbababbababba", "bbbbbbbabbbababbabaabababaab",
           "aaaababaabbbbabaaaaabaaaaabb", "bbaaabbbbabbaaabbaabbabbaaba", "aabaabbbbaabaabbabaabababaaa",
           "abbababbbaababaabbababababbb", "aabbbabbaaaababbbbabbababbbb", "babbbaabababbbbbbbbbaabbabaa"]
    board2 = []
    words2 = ["baabab", "abaaaa", "abaaab", "ababba", "aabbab", "aabbba", "aabaab"]
    for s in lst: board2.append(list(s))
    print(solution.findWords(board2, words2))
