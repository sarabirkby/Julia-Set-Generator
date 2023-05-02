import util


class Arithmetic:
    def __init__(self, threshold, iter_max, coefficients, shades):
        self.threshold = threshold
        self.iter_max = iter_max
        self.coefficients = coefficients
        self.degree: int = len(self.coefficients) - 1
        self.shades = shades
        self.max_value = 0
        self.color = None




class Pixel:
    def __init__(self, arithmetic, real_val, imag_val):
        self.arithmetic = arithmetic
        self.complex_value: complex = real_val + imag_val * 1j
        self.find_iter_num()
        if self.iter_num > self.arithmetic.max_value:
            self.arithmetic.max_value = self.iter_num
        self.color = None

    def find_iter_num(self):
        z: complex = 0
        iter_num = 0
        while iter_num < self.arithmetic.iter_max:
            val = 0
            for k in range(0, self.arithmetic.degree+1):
                val += self.arithmetic.coefficients[k] * (z ** (self.arithmetic.degree-k))
            z = val + self.complex_value
            if abs(z) >= self.arithmetic.threshold:
                self.iter_num = iter_num
                return
            iter_num += 1
        self.iter_num = -1

    def find_color(self):
        if self.iter_num == -1:
            self.color = 0, 0, 0
            return
        per_shade = 255 / self.arithmetic.shades
        std_dev = self.arithmetic.max_value / 12
        red_weight = util.weighted_gaussian(self.iter_num, 0 * self.arithmetic.max_value / 3, std_dev)
        red_weight += util.weighted_gaussian(self.iter_num, 3 * self.arithmetic.max_value / 3, std_dev)
        green_weight = util.weighted_gaussian(self.iter_num, 1 * self.arithmetic.max_value / 3, std_dev)
        blue_weight = util.weighted_gaussian(self.iter_num, 2 * self.arithmetic.max_value / 3, std_dev)
        red = int(red_weight * self.arithmetic.shades) * per_shade
        green = int(green_weight * self.arithmetic.shades) * per_shade
        blue = int(blue_weight * self.arithmetic.shades) * per_shade
        self.color = int(red), int(green), int(blue)

    def find_color_test(self):
        red = (self.complex_value.imag + 2) * (255 / 3)
        return int(red), 0, 0