from gui import *

class Controller:
    """
    The main controller of the operations of the program.
    This object contains a window, and the widgets and main display.
    It also calls and retrieves values from the numbers.py file.
    """
    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x300')
        self.window.resizable(False, False)

        self.widgets = Widgets(self.window)

    def running_loop(self):
        while True:
            self.window.mainloop()
