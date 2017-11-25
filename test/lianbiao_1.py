class Node(object):
    value = None
    n_node = None
    p_node = None
    is_head = False
    is_tail = True

class lb(object):

    def __init__(self, node):
        self.node = node

    def add_node(self, node):
        while self.node.n_node:
            self.node = self.node.n_node
        self.node.is_tail = False
        self.node.n_node = node




if __name__ == "__main__":
    node = Node()
    node.value = "北京"
    node.is_head = True
