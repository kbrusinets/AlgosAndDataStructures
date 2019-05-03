from perfect_hashing import first_greater_prime, get_random_hashing_polynom, execute_hashing
import math

def get_optimal_bit_list_length(number, probability):
    return -(number * math.log(probability))/(math.log(2) ** 2)

def get_optimal_hash_func_number(probability):
    return -math.log2(probability)

class BloomFilter:
    def __init__(self, values, probability, populate=True):
        self.filter = [0] * math.ceil(get_optimal_bit_list_length(len(values), probability))
        self.prime = first_greater_prime(len(self.filter))
        self.hashes = []
        for i in range(math.ceil(get_optimal_hash_func_number(probability))):
            self.hashes.append(get_random_hashing_polynom(self.prime))
        if populate:
            for value in values:
                self.insert(value)

    def insert(self, key):
        for hash in self.hashes:
            self.filter[execute_hashing(key, hash, self.prime, len(self.filter))] = 1

    def contains(self, key):
        answer = True
        for hash in self.hashes:
            answer = answer and bool(self.filter[execute_hashing(key, hash, self.prime, len(self.filter))])
        return answer

'''
bloom_filter = BloomFilter([56,23,87,64,12,82], 0.001)
bloom_filter.insert(15)
print(bloom_filter.filter)
for i in range(0, 100):
    print(str(i) + ' ' + str(bloom_filter.contains(i)))
'''