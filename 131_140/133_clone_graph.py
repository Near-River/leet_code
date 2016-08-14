#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

OJ's undirected graph serialization:

Nodes are labeled uniquely.
We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

    First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
    Second node is labeled as 1. Connect node 1 to node 2.
    Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.

Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

"""


# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution(object):
    def __init__(self):
        self.map = {}

    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        # solution one
        if node is None: return None
        copy_node = UndirectedGraphNode(node.label)
        stack = [node]
        map = {node.label: copy_node}
        while stack:
            _node = stack.pop()
            _copy_node = map[_node.label]
            for neighbor in _node.neighbors:
                if neighbor not in map:
                    _neighbor = UndirectedGraphNode(neighbor.label)
                    _copy_node.neighbors.append(_neighbor)
                    map[neighbor.label] = _neighbor
                    stack.append(neighbor)
                else:
                    _copy_node.neighbors.append(map[neighbor.label])
        # return copy_node

        # solution two
        if node is None: return None
        if node.label in self.map: return self.map[node.label]
        root = UndirectedGraphNode(node.label)
        self.map[node.label] = root
        for neighbor in node.neighbors: root.neighbors.append(self.cloneGraph(neighbor))
        return root


if __name__ == '__main__':
    solution = Solution()
