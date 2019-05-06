import math

def karatsuba_multiplication(first, second):
    if len(first) <= 4 and len(second) <= 4:
        return str(int(first) * int(second))
    max_size = max(len(first), len(second))
    half_size = math.ceil(max_size / 2)
    max_size = half_size * 2
    if len(first) > half_size:
        a = first[0:len(first) - half_size]
        b = first[len(first) - half_size:len(first)]
    else:
        a = '0'
        b = first
    if len(second) > half_size:
        c = second[0:len(second) - half_size]
        d = second[len(second) - half_size:len(second)]
    else:
        c = '0'
        d = second
    z1 = karatsuba_multiplication(a, c)
    z2 = karatsuba_multiplication(b, d)
    z3 = karatsuba_multiplication(long_sum(a, b), long_sum(c, d))
    z3 = long_subtraction(z3, z1)
    z3 = long_subtraction(z3, z2)
    if z1 != '0':
        z1 = z1 + ''.ljust(max_size, '0')
    if z3 != '0':
        z3 = z3 + ''.ljust(half_size, '0')
    answer = long_sum(z1, z3)
    answer = long_sum(answer, z2)
    return answer


def long_sum(first, second):
    first = [int(s) for s in first]
    second = [int(s) for s in second]
    if len(first) < len(second):
        first, second = second, first
    leftover = 0
    i = 0
    append = False
    second_number_ended = False
    while (True):
        if len(first) - 1 - i < 0:
            first_number = 0
            append = True
        else:
            first_number = first[len(first) - 1 - i]
        if len(second) - 1 - i < 0:
            second_number = 0
            second_number_ended = True
        else:
            second_number = second[len(second) - 1 - i]
        sum = first_number + second_number + leftover
        leftover = sum // 10
        if sum > 0:
            if append:
                first = [sum % 10] + first
            else:
                first[len(first) - 1 - i] = sum % 10
        if second_number_ended and leftover == 0:
            break
        i += 1
    return ''.join(str(s) for s in first)


def long_subtraction(first, second):
    first = [int(s) for s in first]
    second = [int(s) for s in second]
    for i in range(0, len(second)):
        first_number = first[len(first)-1-i]
        second_number = second[len(second)-1-i]
        if first_number < second_number:
            j = 1
            while (True):
                if first[len(first) - 1 - i - j] == 0:
                    first[len(first) - 1 - i - j] = 9
                    j += 1
                else:
                    first[len(first) - 1 - i - j] -= 1
                    break
            first_number += 10
        first[len(first) - 1 - i] = first_number - second_number
    if len(first) > 1:
        start_index = next((i for i, x in enumerate(first) if x), len(first) - 1)
    else:
        start_index = 0
    return ''.join(str(s) for s in first[start_index: len(first)])

a = 957898799994567785720006879879
b = 25682345245874567946725456


print(int(karatsuba_multiplication(str(a), str(b))) == a*b)