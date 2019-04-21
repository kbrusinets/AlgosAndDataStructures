def hoare_partition(list, start, end, pivot_value=None):
    left, right = start, end
    if pivot_value == None:
        pivot_value = list[right]

    while True:
        while list[left] < pivot_value:
            left += 1

        while list[right] > pivot_value:
            right -= 1

        if left >= right:
            return left

        list[left], list[right] = list[right], list[left]
        left += 1
        right -= 1


def lomuto_partition(x, start, end):
    pivot = x[end]
    i = start
    for j in range(start, end):
        if x[j] < pivot:
            x[i], x[j] = x[j], x[i]
            i += 1
    x[i], x[end] = x[end], x[i]
    return i