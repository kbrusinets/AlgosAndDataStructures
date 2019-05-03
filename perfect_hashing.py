from random import randint
import math
import numpy


def is_prime(number):
    if miller_rabin(number):
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            if number % i == 0:
                return False
        return True
    return False


def miller_rabin(number):
    def miller_rabin_inner_circle(number, t, power_of_two):
        a = randint(1, number - 1)
        x = pow(a, t, number)
        if (x == 1) or (x == number - 1):
            return True
        for power in range(power_of_two - 1):
            x = pow(x, 2, number)
            if x == 1:
                return False
            elif x == number - 1:
                return True
            else:
                continue
        return False

    if number == 0:
        return False
    elif number == 1:
        return False
    elif number == 2:
        return True
    else:
        t = number - 1
        power_of_two = 0
        while t % 2 == 0:
            t = t // 2
            power_of_two += 1
        for _ in range(int(math.log2(number))):
            if not miller_rabin_inner_circle(number, t, power_of_two):
                return False
        return True


def first_greater_prime(number):
    number += 1
    while True:
        if is_prime(number):
            return number
        number += 1


def get_random_hashing_polynom(prime):
    return [randint(1, prime-1), randint(0, prime-1)]


def execute_hashing(x, polynom, p, n):
    return numpy.polyval(polynom, x) % p % n


def perfect_hashing(values):
    m = len(values)
    n = m
    greater_prime = first_greater_prime(n)
    while True:
        root_hash = [[]] * n
        root_hashing = get_random_hashing_polynom(greater_prime)
        for value in values:
            hash = execute_hashing(value, root_hashing, greater_prime, n)
            if len(root_hash[hash]) is 0:
                root_hash[hash] = [value]
            else:
                root_hash[hash].append(value)
        secondary_hashes_length_sum = 0
        for item in root_hash:
            secondary_hashes_length_sum += len(item) ** 2
        if secondary_hashes_length_sum <= 3 * m:
            break
    for ind, item in enumerate(root_hash):
        while True:
            temp_list = [None] * len(item) ** 2
            greater_prime = first_greater_prime(len(temp_list))
            item_hashing = get_random_hashing_polynom(greater_prime)
            collisions = False
            for value in item:
                hash = execute_hashing(value, item_hashing, greater_prime, len(temp_list))
                if temp_list[hash] is not None:
                    collisions = True
                    break
                else:
                    temp_list[hash] = value
            if not collisions:
                root_hash[ind] = temp_list
                break
    return root_hash

a = []
for i in range(10):
    a.append(randint(0,100))
print(perfect_hashing(a))