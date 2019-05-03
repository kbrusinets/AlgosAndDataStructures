from bloom_filter import BloomFilter

class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class DoubleBloom:
    def __init__(self, values, probability):
        self.zero_bloom = BloomFilter(values, probability, False)
        self.one_bloom = BloomFilter(values, probability, False)
        self.next_level = None

    def insert(self, key, value):
        if value == '0':
            self.zero_bloom.insert(key)
        else:
            self.one_bloom.insert(key)

    def get_value(self, key):
        if self.zero_bloom.contains(key):
            if self.one_bloom.contains(key):
                if self.next_level is not None:
                    return self.next_level.get_value(key)
                return 'Both'
            return '0'
        elif self.one_bloom.contains(key):
            return '1'
        return None

    def add_level(self, values, probability):
        self.next_level = DoubleBloom(values, probability)

class BloomierFilter:
    def __init__(self, key_values, probability):
        self.probability = probability
        self.key_values = []
        self.layers = []
        for i in range(8):
            self.layers.append(DoubleBloom(key_values, probability))
        for key_value in key_values:
            self.insert(key_value)

    def insert(self, key_value):
        ord_char = format(ord(key_value.value), 'b').zfill(8)
        for ind, bit in enumerate(ord_char):
            self.layers[ind].insert(key_value.key, bit)
        self.key_values.append(key_value)

    def get_value(self, key):
        bits = []
        for index, layer in enumerate(self.layers):
            answer = layer.get_value(key)
            if answer == 'Both':
                while True:
                    new_level_elements = []
                    for key_value in self.key_values:
                        if layer.get_value(key_value.key) == 'Both':
                            new_level_elements.append(key_value)
                    layer.add_level(new_level_elements, self.probability)
                    for key_value in new_level_elements:
                        value = format(ord(key_value.value), 'b').zfill(8)[index]
                        layer.next_level.insert(key_value.key, value)
                    answer = layer.get_value(key)
                    if answer == 'Both':
                        layer = layer.next_level
                        continue
            if answer == None:
                return None
            else:
                bits.append(answer)
        return chr(int(''.join(bits), 2))

bloomier_filter = BloomierFilter([KeyValue(1,'a'), KeyValue(2,'b'), KeyValue(3,'c'), KeyValue(4,'d')], 0.001)
k = format(ord('a'), 'b')
print(bloomier_filter.get_value(1))
print(bloomier_filter.get_value(2))
print(bloomier_filter.get_value(3))
print(bloomier_filter.get_value(4))
print(bloomier_filter.get_value(5))