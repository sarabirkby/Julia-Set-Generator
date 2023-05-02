from controller import *
import sys

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700


if __name__ == '__main__':
    contr = Controller(WINDOW_WIDTH, WINDOW_HEIGHT)
    contr.running_loop()
    sys.exit()