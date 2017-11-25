from .Node import Node
class Node(object):
    head = None
    tail = None
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}

    def set_head(self, node):
        if self.head:
            self.head.pre = node
            node.nex = self.head

    def remove_node(self, node):
        if node.pre:
            node.pre.nex = node.nex

        if node.nex:
            node.nex.pre = node.pre

    def add_node(self, key, value):
        node = Node(key, value)
        if key in self.map:
            old = self.map[key]
            old.value = value
        else:
            
