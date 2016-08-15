#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implement a trie with insert, search, and startsWith methods.

Note: You may assume that all inputs are consist of lowercase letters a-z.
"""


# class TrieNode(object):
#     def __init__(self, alpha=None):
#         """
#         Initialize your data structure here.
#         """
#         self.alpha = alpha
#         self.isKey = False
#         self.childrens = []
#
#
# class Trie(object):
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, word):
#         """
#         Inserts a word into the trie.
#         :type word: str
#         :rtype: void
#         """
#         curr = self.root
#         for ch in word:
#             flag = False
#             for child in curr.childrens:
#                 if child.alpha == ch:
#                     flag = True
#                     curr = child
#                     break
#             if not flag:
#                 node = TrieNode(ch)
#                 curr.childrens.append(node)
#                 curr = node
#         curr.isKey = True
#
#     def search(self, word):
#         """
#         Returns if the word is in the trie.
#         :type word: str
#         :rtype: bool
#         """
#         curr = self.root
#         for ch in word:
#             flag = False
#             for child in curr.childrens:
#                 if child.alpha == ch:
#                     flag = True
#                     curr = child
#                     break
#             if not flag: return False
#         return curr.isKey
#
#     def startsWith(self, prefix):
#         """
#         Returns if there is any word in the trie
#         that starts with the given prefix.
#         :type prefix: str
#         :rtype: bool
#         """
#         curr = self.root
#         for ch in prefix:
#             flag = False
#             for child in curr.childrens:
#                 if child.alpha == ch:
#                     flag = True
#                     curr = child
#                     break
#             if not flag: return False
#         return True

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isKey = False
        self.childrens = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for ch in word:
            if ch in curr.childrens:
                curr = curr.childrens[ch]
            else:
                node = TrieNode()
                curr.childrens[ch] = node
                curr = node
        curr.isKey = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for ch in word:
            if ch not in curr.childrens: return False
            curr = curr.childrens[ch]
        return curr.isKey

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for ch in prefix:
            if ch not in curr.childrens: return False
            curr = curr.childrens[ch]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert('abc')
    trie.insert('abc')
    print(trie.search('xyz'))
    print(trie.search('abc'))
    print(trie.search('ab'))
    print(trie.startsWith('abc'))
