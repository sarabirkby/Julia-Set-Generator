from gui import *
from pixel import *
import util
import time

from PIL import Image as Im
from PIL import ImageTk
import numpy as np

CANVAS_WIDTH = 2000
class Controller:
    """
    The main controller of the Mandelbrot & Friends program. Creates an object for
    the GUI, and is responsible for ensuring proper inputs and creating an image
    using the result for each pixel.
    """

    def __init__(self, width, height):
        self.window_width = width
        self.window_height = height
        window_size = f'{width}x{height}'
        self.window = Tk()
        self.window.geometry(window_size)
        self.window.resizable(False, False)

        self.gui = GUI(self.window, self, width)

    def running_loop(self):
        while True:
            self.gui.window.mainloop()

    def generate_picture(self):
        self.gui.generation_beginning()
        pixels = self.generate_pixels()
        self.get_colors(pixels)
        y, x = len(pixels), len(pixels[0])
        file_name = f'images/mandel{int(time.time())}.png'
        img = Im.new(mode="RGB", size=(x, y))
        for i in range(y):
            for j in range(x):
                img.putpixel((j, i), pixels[i][j].color)
                #print(pixels[i][j].color)
        img.save(file_name)

        tkimg = PhotoImage(file=file_name)
        self.gui.display_image(tkimg)

    def generate_pixels(self):

        coefficients = self.gui.coefficient_entry.get()
        iterations = self.gui.iteration_entry.get()
        threshold = self.gui.threshold_entry.get()
        shades = self.gui.shade_num_entry.get()

        min_real = self.gui.min_real_entry.get()
        max_real = self.gui.max_real_entry.get()
        min_imag = self.gui.min_imag_entry.get()
        max_imag = self.gui.max_imag_entry.get()

        if not coefficients:
            coefficients = [1, 0, 0]
        if not iterations:
            iterations = 50
        if not threshold:
            threshold = 2
        if not shades:
            shades = 255
        if not min_real:
            min_real = -2
        if not max_real:
            max_real = 1
        if not min_imag:
            min_imag = -1
        if not max_imag:
            max_imag = 1

        if values := self.check_inputs(coefficients, iterations, threshold, shades,
                                       min_real, max_real, min_imag, max_imag):
            global CANVAS_WIDTH
            self.gui.generation_beginning()
            coefficients, iterations, threshold, shades = values[0], values[1], values[2], values[3]
            real_min, real_max = values[4], values[5]
            imag_min, imag_max = values[6], values[7]
            arithmetic = Arithmetic(threshold, iterations, coefficients, shades)
            self.canvas_width = CANVAS_WIDTH
            self.canvas_height = int(((imag_max - imag_min) / (real_max - real_min)) * self.canvas_width)
            pixels = []
            for y in range(self.canvas_height):
                pixels.append([])
                for x in range(self.canvas_width):
                    real_val = util.get_scaled_value(x, (0, self.canvas_width), (real_min, real_max))
                    imag_val = util.get_scaled_value(y, (0, self.canvas_height),  (imag_max, imag_min))
                    #if self.canvas_width / 6 <= x <= self.canvas_width / 3 and self.canvas_height / 2 <= y <= 5 * self.canvas_height / 6:
                        #print(f'{x}, {y}, {real_val:.2f}, {imag_val:.2f}', end=' | ')
                    pixel = Pixel(arithmetic, real_val, imag_val)
                    pixels[y].append(pixel)
            return pixels

        else:
            self.gui.generation_failed()
            return False

    @staticmethod
    def get_colors(pixels):
        for i in range(len(pixels)):
            for j in range(len(pixels[i])):
                pixels[i][j].find_color()


    @staticmethod
    def check_inputs(coefficients, iterations, threshold, shades, min_real, max_real,
                     min_imag, max_imag):
        try:
            if isinstance(coefficients, str):
                coefficients = coefficients.split(',')
                coefficients = [float(coefficient.strip()) for coefficient in coefficients]
            iterations = int(iterations)
            threshold = float(threshold)
            min_real = float(min_real)
            max_real = float(max_real)
            min_imag = float(min_imag)
            max_imag = float(max_imag)
            shades = int(shades)
        except:
            print('Input failure 1')
            return False
        else:
            if not util.check_if_greater_than(threshold, shades, iterations):
                return False
            if not (max_real > min_real and max_imag > min_imag):
                return False
            for coefficient in coefficients:
                if not coefficient >= 0:
                    print('test3')
                    return False
            return coefficients, int(iterations), float(threshold), int(shades), float(min_real),\
                   float(max_real), float(min_imag), float(max_imag)


