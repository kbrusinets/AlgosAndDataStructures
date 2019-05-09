def second_large(array, start, finish):
    length = finish - start
    if length == 2:
        if array[start] >= array[start + 1]:
            return array[start], [array[start + 1]]
        else:
            return array[start + 1], [array[start]]
    left_max, left_supposed = second_large(array, start, start + length // 2)
    right_max, right_supposed = second_large(array, start + length // 2, finish)
    if left_max >= right_max:
        left_supposed.append(right_max)
        return left_max, left_supposed
    else:
        right_supposed.append(left_max)
        return right_max, right_supposed

def find_second_large(array):
    max, supposed_second = second_large(array, 0, len(array))
    second_max = supposed_second[0]
    for i in supposed_second:
        if i > second_max:
            second_max = i
    return second_max


a = [9,4,1,5,2,3,4,6]

print(find_second_large(a))