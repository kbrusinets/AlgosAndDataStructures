from random import randint
from partitions import hoare_partition
from math import ceil

def get_order_statistics(list, start, end, order):
    while start < end:
        pivot_value = get_pivot_by_five(list, start, end)
        pivot = hoare_partition(list, start, end, pivot_value)
        if pivot - start > order - 1:
            return get_order_statistics(list, start, pivot - 1, order)
        else:
            order -= pivot - start
            start = pivot
    if order == 1:
        return list[start]


def selection_sort(list, start, end):
    if start < len(list):
        for i in range(start, min(end, len(list))):
            minimum = i
            for j in range(i+1, min(end+1, len(list))):
                if list[j] < list[minimum]:
                    minimum = j
            list[i], list[minimum] = list[minimum], list[i]


def get_pivot_by_five(list, start, end):
    order_of_pack = 0
    length = end - start + 1
    if length < 3:
        return list[end]
    while 2 + (order_of_pack * 5) < length:
        selection_sort(list, order_of_pack * 5, order_of_pack * 5 + 4)
        order_of_pack += 1
    medians = [v for i, v in enumerate(list[start:end+1]) if i in range(2, length, 5)]
    return get_order_statistics(medians, 0, len(medians)-1, ceil(len(medians)/2))




a = [1,2]
for i in range(len(a)):
    i += 1
    print(get_order_statistics(a, 0, len(a)-1, i))