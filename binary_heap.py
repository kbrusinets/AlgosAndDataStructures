class BinaryHeap:
    def __init__(self, values_list=None):
        if values_list is None:
            values_list = []
        self.nodes = [None] * len(values_list)
        self.last_index = len(self.nodes) - 1
        last_i = len(values_list) - 1
        first_instant_insert_i = int((last_i - 1)/2) + 1
        i = first_instant_insert_i
        while i < len(values_list):
            self.nodes[i] = values_list[i]
            i += 1
        i = first_instant_insert_i - 1
        while i >= 0:
            self.nodes[i] = values_list[i]
            self.sift_down(i)
            i -= 1

    def sift_down(self, index):
        while True:
            if 2*index + 1 <= self.last_index:
                index_with_min = 2*index + 1
            else:
                return index
            if 2*index + 2 <= self.last_index and self.nodes[2*index + 2] < self.nodes[2*index + 1]:
                index_with_min = 2*index + 2
            if self.nodes[index_with_min] < self.nodes[index]:
                self.nodes[index_with_min], self.nodes[index] = self.nodes[index], self.nodes[index_with_min]
                index = index_with_min
            else:
                return index

    def sift_up(self, index):
        while True:
            if index > 0:
                if self.nodes[int((index - 1)/2)] > self.nodes[index]:
                    self.nodes[int((index - 1)/2)], self.nodes[index] = self.nodes[index], self.nodes[int((index - 1)/2)]
                    index = int((index - 1)/2)
                else:
                    return index
            else:
                return index

    def insert(self, key):
        self.last_index += 1
        self.nodes[self.last_index] = key
        self.sift_up(self.last_index)

    def get_min(self):
        return self.nodes[0]

    def extract_min(self):
        if self.last_index < 0:
            return None
        answer = self.nodes[0]
        self.nodes[0], self.nodes[self.last_index] = self.nodes[self.last_index], None
        self.last_index -= 1
        self.sift_down(0)
        return answer

    def decrease_key(self, index, key):
        if key > self.nodes[index]:
            raise ValueError("When decreasing, new key must be lesser or equal than present key.")
        self.nodes[index] = key
        return self.sift_up(index)

    def remove(self, index):
        if index < 0 or index > self.last_index:
            raise ValueError("Index must be grater than zero and lesser than last index.")
        if index == self.last_index:
            self.nodes[index] = None
            self.last_index -= 1
        else:
            self.nodes[index], self.nodes[self.last_index] = self.nodes[self.last_index], None
            self.last_index -= 1
            if self.nodes[index] < self.nodes[int((index - 1)/2)]:
                self.sift_up(index)
            else:
                self.sift_down(index)



a = BinaryHeap([5,4,3,2,1,10])
