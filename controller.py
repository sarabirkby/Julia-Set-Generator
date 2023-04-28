from gui import *
import util

import PIL


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
        degree = self.gui.degree_entry.get()
        coefficients = self.gui.coefficient_entry.get()
        iterations = self.gui.iteration_entry.get()
        threshold = self.gui.threshold_entry.get()

        min_real = self.gui.min_real_entry.get()
        max_real = self.gui.max_real_entry.get()
        min_imag = self.gui.min_imag_entry.get()
        max_imag = self.gui.max_imag_entry.get()

        if values := self.check_inputs(degree, coefficients, iterations, threshold,
                                 min_real, max_real, min_imag, max_imag):
            self.gui.generation_succeeded()
            self.canvas_width = 0.9 * self.window_width
            widget_height = self.gui.widget_frame.winfo_height()
            self.canvas_height = 0.9 * (self.window_height - widget_height)
            pixels = ([None] * self.window_width) * self.window_height
            for y in self.window_height:
                for x in self.window_width:
                    pixel_real_val = util.get_scaled_value(x, (min_real, max_real),
                                                           (0, self.canvas_width))
                    pixel_imag_val = util.get_scaled_value(y, (min_imag, max_imag),
                                                           (0, self.canvas_height))
        else:
            self.gui.generation_failed()




    @staticmethod
    def check_inputs(degree, coefficients, iterations, threshold, min_real, max_real,
                     min_imag, max_imag):
        try:
            degree = int(degree)
            coefficients = coefficients.split(',').strip()
            coefficients = [float(coefficient) for coefficient in coefficients]
            iterations = int(iterations)
            threshold = float(threshold)
            min_real = float(min_real)
            max_real = float(max_real)
            min_imag = float(min_imag)
            max_imag = float(max_imag)
        except:
            return False
        else:
            if len(coefficients) != degree + 1:
                return False
            if not util.check_if_greater_than(degree, threshold, min_real, max_real,
                                      min_imag, max_imag):
                return False
            for coefficient in coefficients:
                if not util.check_if_greater_than(coefficient):
                   return False

            return degree, coefficients, iterations, threshold, min_real, max_real, min_imag, max_imag


