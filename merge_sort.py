import math

def merge_sort(list):
    for k in range (0, int(math.log2(len(list)))+1):
        length = 2**k
        start_first, start_second, finish_second = 0, length, min(len(list), length*2)
        while start_second < len(list):
            merge(list, start_first, start_second, finish_second)
            start_first += 2*length
            start_second += 2*length
            finish_second = min(finish_second + 2*length, len(list))


def merge(list, start_first, start_second, finish_second):
    buffer = list[start_first:start_second].copy()
    i, j, k = start_first, 0, start_second
    while j < len(buffer):
        if k < finish_second:
            if buffer[j] <= list[k]:
                list[i] = buffer[j]
                i += 1
                j += 1
            else:
                list[i] = list[k]
                i += 1
                k += 1
        else:
            list[i:finish_second] = buffer[j:len(buffer)]
            break