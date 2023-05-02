import math


def check_if_greater_than(*numbers, value=0):
    for number in numbers:
        if number < value:
            return False
    return True


def get_scaled_value(value: float, initial_range, final_range):
    input_dist = initial_range[1] - initial_range[0]
    output_dist = final_range[1] - final_range[0]
    input_weight = (value - initial_range[0]) / input_dist
    return input_weight * output_dist + final_range[0]



def calculate_gaussian_function(x, mean, std):
    coeff = 1 / (std * math.sqrt(2 * math.pi))
    power = -((x - mean) ** 2 / std ** 2) / 2
    return coeff * math.e ** power


def weighted_gaussian(x, mean, std):
    return calculate_gaussian_function(x, mean, std) / calculate_gaussian_function(mean, mean, std)


def mandelbrot_test(c: complex, threshold: float, max_iterations: int):
    z, iter_num = 0, 0
    while iter_num < max_iterations:
        square = z ** 2
        z = square + c
        val = abs(z)
        if val >= threshold:
            return iter_num
        iter_num += 1
    return -1


def get_highest_val(iterable):
    items = []
    for i in range(len(iterable)):
        for item in iterable[i]:
            items.append(abs(item.complex_value))
    return max(items)
