import math

def quick_sort_hoare(list):
    _quick_sort_hoare(list, 0, len(list) - 1)


def _quick_sort_hoare(list, start, end):
    while start < end:
        pivot = hoare_partition(list, start, end)
        _quick_sort_hoare(list, start, pivot-1)
        start = pivot


def hoare_partition(list, start, end):
    left, right = start, end
    pivot = list[right]

    while True:
        while list[left] < pivot:
            left += 1

        while list[right] > pivot:
            right -= 1

        if left >= right:
            return left

        list[left], list[right] = list[right], list[left]
        left += 1
        right -= 1


def quick_sort_lomuto(list):
    _quick_sort_lomuto(list, 0, len(list)-1)


def _quick_sort_lomuto(list, start, end):
    while start < end:
        pivot = lomuto_partition(list, start, end)
        _quick_sort_lomuto(list, start, pivot-1)
        start = pivot + 1


def lomuto_partition(x, start, end):
    pivot = x[end]
    i = start
    for j in range(start, end):
        if x[j] < pivot:
            x[i], x[j] = x[j], x[i]
            i += 1
    x[i], x[end] = x[end], x[i]
    return i


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




a = [5,4,3,2,1,2,3,4,5]
b = a.copy()
c = a.copy()
quick_sort_lomuto(a)
print(a)
quick_sort_hoare(b)
print(b)
merge_sort(c)
print(c)



