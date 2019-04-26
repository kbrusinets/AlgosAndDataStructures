import copy

class BinomialTree:
    def __init__(self, key):
        self.key = key
        self.child = None
        self.right_brother = None
        self.order = 0

    def meld(first_tree, second_tree):
        if second_tree.key <= first_tree.key:
            first_tree, second_tree = second_tree, first_tree
        if first_tree.child is None:
            first_tree.child = second_tree
            first_tree.order += 1
        else:
            last_son = first_tree.child
            while last_son.right_brother is not None:
                last_son = last_son.right_brother
            last_son.right_brother = second_tree
            first_tree.order += 1
        return first_tree

class BinomialHeap:
    def __init__(self, trees=None):
        self.trees = []
        if trees is None:
            trees = []
        for tree in trees:
            self.add_tree(tree)

    def extract_min(self):
        if not self.trees:
            return None
        index_of_tree_with_min = None
        for idx, tree in enumerate(self.trees):
            if tree is not None and (index_of_tree_with_min is None or tree.key < self.trees[index_of_tree_with_min].key):
                index_of_tree_with_min = idx
        minimum = self.trees[index_of_tree_with_min].key
        extracted_tree = self.trees[index_of_tree_with_min]
        self.trees[index_of_tree_with_min] = None
        part_of_extracted = extracted_tree.child
        while part_of_extracted is not None:
            self.add_tree(part_of_extracted)
            right_brother = part_of_extracted.right_brother
            part_of_extracted.right_brother = None
            part_of_extracted = right_brother
        return minimum

    def add_tree(self, new_tree):
        while new_tree is not None:
            if new_tree.order >= len(self.trees):
                self.trees.extend([None] * (new_tree.order - (len(self.trees) - 1)))
            if self.trees[new_tree.order] is None:
                self.trees[new_tree.order] = new_tree
                new_tree = None
            else:
                popped_tree = self.trees[new_tree.order]
                self.trees[new_tree.order] = None
                new_tree = BinomialTree.meld(new_tree, popped_tree)

    def meld(self, new_heap):
        for tree in new_heap.trees:
            self.add_tree(tree)
            #Если не делать копию, то портится вторая куча. Но сложность копии O(n). Что делать?
            #self.add_tree(copy.deepcopy(tree))

    def get_min(self):
        if not self.trees:
            return None
        minimum = None
        for tree in self.trees:
            if tree is not None and (minimum is None or tree.key < minimum):
                minimum = tree.key
        return minimum

    def insert(self, key):
        self.add_tree(BinomialTree(key))

a = BinomialHeap()
a.insert(5)
a.insert(6)
a.insert(7)
a.insert(8)
a.insert(3)
a.insert(1)
b = BinomialHeap()
b.insert(0)
b.insert(5)
b.insert(20)
b.insert(-2)
b.insert(6)
a.meld(b)
