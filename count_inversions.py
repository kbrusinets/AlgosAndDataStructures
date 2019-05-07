def count_inversions(array, start, finish):
    length = finish - start
    if length == 0 or length == 1:
        return 0
    start_second = start + length // 2
    left = count_inversions(array, start, start_second)
    right = count_inversions(array, start_second, finish)
    splitted = merge_and_count_inv(array, start, start_second, finish)
    return left + right + splitted

def merge_and_count_inv(array, start_first, start_second, finish):
    i = 0
    j = 0
    k = 0
    inversions = 0
    buffer = array[start_first:start_second]
    while (start_first + k < start_second + j):
        if (start_second + j < finish and buffer[i] <= array[start_second + j]) or start_second + j >= finish:
            array[start_first + k] = buffer[i]
            k += 1
            i += 1
        else:
            inversions += len(buffer) - i
            array[start_first + k] = array[start_second + j]
            k += 1
            j += 1
    return inversions

a = [3,4,6,1,2,5]

print (count_inversions(a, 0, len(a)))