import math


def get_max_circles_in_rectangle2(short_length, long_length):
    triangle_pattern_t = pow(3, 1 / 2) / 2
    max_triangle_row = math.floor(short_length / triangle_pattern_t)
    # print(max_triangle_row)
    all_list = list()
    for triangle_pattern_row in range(max_triangle_row + 1):

        total_circles = long_length + 1
        for i in range(triangle_pattern_row):
            if i % 2 == 0:
                total_circles += long_length
            else:
                total_circles += (long_length + 1)
        # rectangle_pattern_part
        remain_length = math.floor(short_length - triangle_pattern_row * triangle_pattern_t - 1)
        for i in range(remain_length + 1):
            total_circles += (long_length + 1)

        all_list.append(total_circles)
    return max(all_list)


def result_answer(short_length, long_length):
    a = get_max_circles_in_rectangle2(short_length, long_length)
    b = get_max_circles_in_rectangle2(long_length, short_length)
    if a >= b:
        return a
    else:
        return b


print(result_answer(8, 9))
print(result_answer(10, 10))
print(result_answer(61, 67))
print(result_answer(53, 59))
