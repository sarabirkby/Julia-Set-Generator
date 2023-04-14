from tkinter import *

class Widgets:
    def __init__(self, window):
        self.window = window

        self.color_selection = IntVar()
        self.color_selection.set(0)
        self.input_func_degree = StringVar()
        self.input_func_degree.set('')


        self.title_message = Label(self.window, text='Julia Set Generator', font=("Arial", 18))
        self.iter_color_select = Radiobutton(self.window, text='Iteration Count Coloring', variable=self.color_selection, value=1)
        self.converge_color_select = Radiobutton(self.window, text='Convergence Location Coloring', variable=self.color_selection, value=2)
        self.CLC_input_func_degree = Entry(self.window)

        self.title_message.pack(side='top', pady=10)
        self.iter_color_select.pack(side='left', padx=10)
        self.converge_color_select.pack(side='left', padx=10)
        self.CLC_input_func_degree.pack(side='left')



