import math

def get_max_circles_in_rectangle(short_length, long_length):
    # triangle_pattern_part
    triangle_pattern_t = pow(3, 1 / 2) / 2
    other_row = math.floor(short_length / triangle_pattern_t * (1 - triangle_pattern_t))
    total_triangle_pattern_row = math.floor(other_row / (1 - triangle_pattern_t))

    total_circles = long_length + 1
    for i in range(total_triangle_pattern_row):
        if i % 2 == 0:
            total_circles += long_length
        else:
            total_circles += (long_length + 1)

    # rectangle_pattern_part
    remain_length = math.floor(short_length - total_triangle_pattern_row * triangle_pattern_t)
    for i in range(remain_length + 1):
        total_circles += (long_length + 1)
    return total_circles


print(get_max_circles_in_rectangle(8, 9))
print(get_max_circles_in_rectangle(10, 10))
