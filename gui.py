import tkinter.tix
from tkinter import *
from util import *



class GUI:
    def __init__(self, window, controller, win_width):
        self.controller = controller
        self.window: object = window

        def gen_frames():
            self.widget_frame = Frame(self.window)
            self.display_frame = Frame(self.window)
            self.widget_frame.grid(row=0, column=0)
            self.display_frame.grid(row=1, column=0)

            self.window.columnconfigure(index=0, weight=1)
            self.widget_frame.columnconfigure(index=0, weight=1)

            self.title_frame = Frame(self.widget_frame)
            self.title_frame.grid(row=0, column=0)

            self.attribute_frame = Frame(self.widget_frame)
            self.attribute_frame.grid(row=1, column=0)

            print(self.attribute_frame.winfo_height())

            self.range_frame = Frame(self.widget_frame)
            self.range_frame.grid(row=2, column=0)

            self.activation_frame = Frame(self.widget_frame)
            self.activation_frame.grid(row=3, column=0)

            self.condition_frame = Frame(self.widget_frame)
            self.condition_frame.grid(row=4, column=0)

            for i in range(6):
                self.range_frame.columnconfigure(index=i, weight=10, minsize=15)
            self.range_frame.columnconfigure(index=1, weight=12)
            self.range_frame.columnconfigure(index=4, weight=12)
            self.range_frame.columnconfigure(index=2, weight=20, minsize=50)


        def gen_widgets():
            # Title Frame
            self.title = Label(self.title_frame, text='Mandelbrot Family Julia Set Generator', font=('Arial', 12))
            self.title.pack(anchor='n', side='top', pady=10)

            # Attribute Frame
            self.degree_label = Label(self.attribute_frame, text='Polynomial Degree (1): ', font=('Arial', 7))
            self.coefficient_label = Label(self.attribute_frame, text='Polynomial (1): ', font=('Arial', 7))
            self.iteration_label = Label(self.attribute_frame, text='Number of Iterations (2): ', font=('Arial', 7))
            self.threshold_label = Label(self.attribute_frame, text='Threshold Value (3): ', font=('Arial', 7))

            self.degree_entry = Entry(self.attribute_frame, width=5, font=('Arial', 7))
            self.coefficient_entry = Entry(self.attribute_frame, width=10, font=('Arial', 7))
            self.iteration_entry = Entry(self.attribute_frame, width=5, font=('Arial', 7))
            self.threshold_entry = Entry(self.attribute_frame, width=5, font=('Arial', 7))

            pack_row( (self.degree_label, 15), (self.degree_entry, 0), (self.coefficient_label, 15),
                           (self.coefficient_entry, 0), (self.iteration_label, 15), (self.iteration_entry, 0),
                           (self.threshold_label, 15), (self.threshold_entry, 0) )

            # Range Frame
            self.min_real_label = Label(self.range_frame, text='Real Min (4): ', font=('Arial', 7))
            self.max_real_label = Label(self.range_frame, text='Real Max: ', font=('Arial', 7))
            self.min_imag_label = Label(self.range_frame, text='Imaginary Min: ', font=('Arial', 7))
            self.max_imag_label = Label(self.range_frame, text='Imaginary Max: ', font=('Arial', 7))
            self.min_i_label = Label(self.range_frame, text='i', font=('Cambria Math', 7))
            self.max_i_label = Label(self.range_frame, text='i', font=('Cambria Math', 7))
            self.min_break = Label(self.range_frame, text=' ')
            self.max_break = Label(self.range_frame, text=' ')

            self.min_real_entry = Entry(self.range_frame, width=5, font=('Arial', 7))
            self.max_real_entry = Entry(self.range_frame, width=5, font=('Arial', 7))
            self.min_imag_entry = Entry(self.range_frame, width=5, font=('Arial', 7))
            self.max_imag_entry = Entry(self.range_frame, width=5, font=('Arial', 7))

            self.place_grid_row(self.min_real_label, self.min_real_entry, self.min_break, self.min_imag_label,
                                self.min_imag_entry, self.min_i_label, row_num=0)
            self.place_grid_row(self.max_real_label, self.max_real_entry, self.max_break, self.max_imag_label,
                                self.max_imag_entry, self.max_i_label, row_num=1)

            # Activation Frame
            self.shade_num_label = Label(self.activation_frame, text='Color Shades (5): ', font=('Arial', 7))
            self.shade_num_entry = Entry(self.activation_frame, width=5, font=('Arial', 7))
            self.generate_button = Button(self.activation_frame, text='Render', command=self.controller.generate_picture)

            pack_row( (self.shade_num_label, 15), (self.shade_num_entry, 0), (self.generate_button, 15) )

            # Failure Frame
            self.failure_label = Label(self.condition_frame, text='Generation Failed! Check inputs.', font=('Arial', 12))
            self.success_label = Label(self.condition_frame, text='Inputs Good, Generating...', font=('Arial', 12))
        gen_frames()
        gen_widgets()

    def generation_failed(self):
        self.success_label.pack_forget()
        self.failure_label.pack()

    def generation_succeeded(self):
        self.failure_label.pack_forget()
        self.success_label.pack()

    @staticmethod
    def place_grid_row(*widgets, row_num=0):
        for i in range(len(widgets)):
            widgets[i].grid(row=row_num, column=i)

    @staticmethod
    def hide_widgets(*widgets):
        for widget in widgets:
            GUI.hide_widget(widget)

    @staticmethod
    def show_widgets(*widgets):
        for widget in widgets:
            GUI.show_widget(widget)

    @staticmethod
    def hide_widget(widget):
        widget.pack_forget()

    @staticmethod
    def show_widget(widget):
        widget.pack()


def pack_row(*items: tuple[object, int]):
    for item in items:
        obj, padding = item[0], item[1]
        obj.pack(side='left', padx=padding)
