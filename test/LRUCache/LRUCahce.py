from Node import Node

class LRU(object):
    head = None
    tail = None
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}

    def set_head(self, node):
        if self.head:
            self.head.pre = node
            node.nex = self.head
        self.head = node

    def remove_node(self, node):
        if node.pre:
            node.pre.nex = node.nex

        if node.nex:
            node.nex.pre = node.pre

    def add_node(self, key, value):
        if key in self.map:
            old = self.map[key]
            old.value = value
            node = old
        else:
            node = Node(key, value)
            self.map[key] = node
        self.remove_node(node)
        self.set_head(node)

    def one_node(self, key):
        if key in self.map:
            node = self.map[key]
            self.remove_node(node)
            self.set_head(node)
            return node
        else:
            return Node

    def all_node(self):
        n = self.head
        while n:
            print(n.key, 10*'=>', n.value)
            n = n.nex


lru = LRU(3)
key = "a"
value = "牛"
lru.add_node(key, value)
key = "b"
value = "张"
lru.add_node(key, value)
key = "c"
value = "马"
lru.add_node(key, value)

key = "d"
value = "猪"
lru.add_node(key, value)

key = "a"
value = "牛牛"
lru.add_node(key, value)

lru.all_node()