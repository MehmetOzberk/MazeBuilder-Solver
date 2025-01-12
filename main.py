from graphics import Window, Line, Point
from maze import Maze
import random
import keyboard 
import os

##test
def exit_on_key(keyname):
    """ Create callback function that exits current process when the key with
        the given name is pressed.
    """
    def callback(event):
        if event.name == keyname:
            os._exit(1)
    return callback


def workload():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin,margin,num_rows,num_cols,cell_size_x,cell_size_y,win, seed = random.randint(1,100))
    maze.solve()
    win.wait_for_close()
    exit()

def main():
    keyboard.hook(exit_on_key("esc"))
    workload()
main()