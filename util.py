def check_if_greater_than(*numbers, value=0):
    for number in numbers:
        if number < value:
            return False
    return True


def get_scaled_value(value, initial_range, final_range):
    return value * scale_weigher(initial_range, final_range) + final_range[0]


def scale_weigher(initial_range, final_range):
    return (initial_range[1] - initial_range[0]) * (final_range[1] - final_range[0])
