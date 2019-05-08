import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point x={}, y={}.".format(self.x, self.y)

    def __repr__(self):
        return "Point x={}, y={}.".format(self.x, self.y)

def compare_points_by_x(point_1, point_2):
    return point_1.x <= point_2.x

def compare_points_by_y(point_1, point_2):
    return point_1.y <= point_2.y

def euclidean_distance(point_1, point_2):
    if point_1 is None or point_2 is None:
        return math.inf
    return math.sqrt( (point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2)

def generate_two_sorted_arrays(array):
    array_x = array.copy()
    merge_sort(array_x, compare_points_by_x)
    array_y = array.copy()
    merge_sort(array_y, compare_points_by_y)
    return array_x, array_y

def merge_sort(array, compare_method):
    for k in range(int(math.log2(len(array)))+1):
        length = 2 ** k
        for i in range(0, len(array), length):
            if i + length < len(array):
                merge(array, i, length, compare_method)

def merge(array, start_first, length, compare_method):
    buffer = array[start_first: start_first + length]
    i = start_first
    j = 0
    finish_second = min(len(array), start_first + 2*length)
    k = start_first + length
    while j < len(buffer):
        if k < finish_second:
            if compare_method(buffer[j], array[k]):
                array[i] = buffer[j]
                i += 1
                j += 1
            else:
                array[i] = array[k]
                i += 1
                k += 1
        else:
            array[i:finish_second] = buffer[j:len(buffer)]
            break

def closest_2d_pair(array):
    array_x, array_y = generate_two_sorted_arrays(array)
    return closest_pair(array_x, array_y)

def closest_pair(array_sorted_by_x, array_sorted_by_y):
    if len(array_sorted_by_x) == 2:
        return array_sorted_by_x[0], array_sorted_by_x[1]
    elif len(array_sorted_by_x) < 2:
        return None, None
    left_x = array_sorted_by_x[:len(array_sorted_by_x) // 2]
    right_x = array_sorted_by_x[len(array_sorted_by_x) // 2:]
    middle_x = left_x[len(left_x) - 1]
    left_y = []
    right_y = []
    for i in array_sorted_by_y:
        if i.x <= middle_x.x:
            left_y.append(i)
        else:
            right_y.append(i)
    p1, q1 = closest_pair(left_x, left_y)
    p2, q2 = closest_pair(right_x, right_y)
    dist_1 = euclidean_distance(p1, q1)
    dist_2 = euclidean_distance(p2, q2)
    delta = min(dist_1, dist_2)
    p3, q3 = closest_split_pair(array_sorted_by_x, array_sorted_by_y, delta)
    dist_3 = euclidean_distance(p3, q3)
    if dist_3 < delta:
        return p3, q3
    elif dist_1 == delta:
        return p1, q1
    else:
        return p2, q2


def closest_split_pair(array_sorted_by_x, array_sorted_by_y, delta):
    if len(array_sorted_by_x) == 2:
        return array_sorted_by_x[0], array_sorted_by_x[1]
    elif len(array_sorted_by_x) < 2:
        return None, None
    p_ans = None
    q_ans = None
    middle_x = array_sorted_by_x[len(array_sorted_by_x) // 2]
    s_y = []
    for i in array_sorted_by_y:
        if abs(i.x - middle_x.x) <= delta:
            s_y.append(i)
    for i in range(len(s_y)):
        for j in range(1, min(8, len(s_y) - i )):
            if euclidean_distance(s_y[i], s_y[i+j]) < delta:
                p_ans = s_y[i]
                q_ans = s_y[i+j]
    return p_ans, q_ans


array = []
array.append(Point(1,2))
array.append(Point(2,10))
array.append(Point(2,500))
array.append(Point(2,510))
array.append(Point(1,9))


print(closest_2d_pair(array))