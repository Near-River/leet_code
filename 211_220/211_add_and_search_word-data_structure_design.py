#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Design a data structure that supports the following two operations:
1.    void addWord(word)
2.    bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can
represent any one letter.

For example:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note: ou may assume that all words are consist of lowercase letters a-z.
"""


class WordDictionary(object):
    class TrieNode(object):
        def __init__(self):
            self.isKey = False
            self.childrens = {}

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = self.TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for ch in word:
            if ch in curr.childrens:
                curr = curr.childrens[ch]
            else:
                node = self.TrieNode()
                curr.childrens[ch] = node
                curr = node
        curr.isKey = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.search_word(self.root, word, 0)

    def search_word(self, root, word, start):
        if start == len(word): return root.isKey
        for i in range(start, len(word)):
            ch = word[i]
            if ch == '.':
                for child in root.childrens:
                    if self.search_word(root.childrens[child], word, i + 1): return True
                return False
            elif ch in root.childrens:
                root = root.childrens[ch]
            else:
                return False
        return root.isKey


if __name__ == '__main__':
    dictionary = WordDictionary()
    dictionary.addWord('a')
    dictionary.addWord('a')
    print(dictionary.search('.'))
    print(dictionary.search('a'))
    print(dictionary.search('aa'))
    print(dictionary.search('a'))
    print(dictionary.search('.a'))
    print(dictionary.search('a.'))
