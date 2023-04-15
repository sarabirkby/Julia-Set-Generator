from tkinter import *
from util import *

# TODO: Add threshold and function input
# TODO: Add upper and lower bounds for display (re and im)

class Widgets:
    def __init__(self, window):
        self.window = window

        self.top_frame = Frame(self.window)
        # F1 - Variables
        self.color_selection = IntVar()
        self.color_selection.set(0)
        # F1 - Widgets
        self.CLC_input_func_degree = Entry(self.top_frame)
        self.title_message = Label(self.top_frame, text='Julia Set Generator', font=("Arial", 18))
        self.iter_color_select = Radiobutton(self.top_frame, text='Iteration Count', font=("Arial", 8),
                                             variable=self.color_selection, value=1, command=self.ICC_mode_widgets)
        self.converge_color_select = Radiobutton(self.top_frame, text='Convergence Location',
                                                 font=("Arial", 8),
                                                 variable=self.color_selection, value=2,
                                                 command=self.CLC_mode_widgets)
        # F1 - Packing
        self.title_message.pack(side='top', pady=10)
        self.iter_color_select.pack(side='left', padx=10)
        self.converge_color_select.pack(side='left', padx=10)
        self.CLC_input_func_degree.pack(side='left', padx=10)
        self.CLC_input_func_degree.pack_forget()
        self.top_frame.pack()

        # Minimum Range Frame
        self.min_range_frame = Frame(self.window)

        self.real_min_label = Label(self.min_range_frame, text='Real min: ', font=("Arial", 8))
        self.real_min_entry = Entry(self.min_range_frame, width=7)
        self.imag_min_label = Label(self.min_range_frame, text='Imaginary min: ', font=("Arial", 8))
        self.imag_min_entry = Entry(self.min_range_frame, width=7)

        self.real_min_label.pack(side='left', padx=5)
        self.real_min_entry.pack(side='left', padx=5)
        self.imag_min_label.pack(side='left', padx=15)
        self.imag_min_entry.pack(side='left', padx=5)
        self.min_range_frame.pack(side='left')

        # ICC Polynomial Frame

        self.ICC_poly_frame = Frame(self.window)
        self.ICC_degree_label = Label(self.ICC_poly_frame, text='Poly. Deg.:', font=("Arial", 8))
        self.ICC_degree_entry = Entry(self.ICC_poly_frame, width=7)

        self.ICC_degree_label.pack(side='left', padx=15)
        self.ICC_degree_entry.pack(side='left', padx=10)
        self.hide_widgets(self.ICC_degree_entry, self.ICC_degree_label)
        self.ICC_poly_frame.pack(side='right',padx=40)

    @staticmethod
    def hide_widgets(*widgets):
        for widget in widgets:
            Widgets.hide_widget(widget)

    @staticmethod
    def show_widgets(*widgets):
        for widget in widgets:
            Widgets.show_widget(widget)

    @staticmethod
    def hide_widget(widget):
        widget.pack_forget()

    @staticmethod
    def show_widget(widget):
        widget.pack()

    def ICC_mode_widgets(self):
        self.hide_widget(self.CLC_input_func_degree)
        self.show_widget(self.ICC_degree_label)
        self.show_widget(self.ICC_degree_entry)

    def CLC_mode_widgets(self):
        self.show_widget(self.CLC_input_func_degree)
        self.hide_widget(self.ICC_degree_entry)
        self.hide_widget(self.ICC_degree_label)



