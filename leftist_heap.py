class LeftistHeapNode:
    def __init__(self, key=None):
        self.key = key
        self.left_child = None
        self.right_child = None
        self.rank = 0

class LeftistHeap:
    def __init__(self, node=None):
        self.root_node = node

    def meld(self, second_heap):
        if self.root_node is None:
            return second_heap.root_node
        elif second_heap.root_node is not None:
            if self.root_node.key <= second_heap.root_node.key:
                self.root_node.right_child = LeftistHeap(self.root_node.right_child).meld(second_heap)
                self.normalize()
                return self.root_node
            else:
                return second_heap.meld(self)
        else:
            return self.root_node

    def normalize(self):
        if self.root_node.left_child is None or (self.root_node.right_child.rank > self.root_node.left_child.rank):
            self.root_node.left_child, self.root_node.right_child = self.root_node.right_child, self.root_node.left_child
        if self.root_node.right_child is None:
            self.root_node.rank = 0
        else:
            self.root_node.rank = self.root_node.right_child.rank + 1

    def get_min(self):
        return self.root_node.key

    def insert(self, key):
        self.root_node = self.meld(LeftistHeap(LeftistHeapNode(key)))

a = LeftistHeap()
a.insert(4)
a.insert(19)
a.insert(8)
a.insert(27)
a.insert(20)
a.insert(12)
a.insert(43)
a.insert(15)
a.insert(25)

b = LeftistHeap()
b.insert(6)
b.insert(8)
b.insert(7)
b.insert(14)

c = LeftistHeap()
c.root_node = a.meld(b)