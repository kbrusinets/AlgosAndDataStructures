def index_eq_element(array, start, finish):
    if finish - start == 1:
        if array[start] == start:
            return start
        else:
            return None
    middle = start + (finish - start) // 2
    if array[middle] == middle:
        return middle
    elif array[middle] > middle:
        return index_eq_element(array, start, middle)
    else:
        return index_eq_element(array, middle, finish)

a = [-7,-5,-3,-1,0,2,6,9,10]

print(index_eq_element(a, 0, len(a)))