def max_in_unimodal(array, start, finish):
    if finish - start == 1:
        return array[start]
    middle = start + (finish - start) // 2
    if array[middle - 1] > array[middle]:
        return max_in_unimodal(array, start, middle)
    else:
        return max_in_unimodal(array, middle, finish)


a = [1,5,4,3,2,1,0]
print(max_in_unimodal(a, 0, len(a)))