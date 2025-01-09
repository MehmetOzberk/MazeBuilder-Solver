import tkinter as tk
from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height, title = "My Window"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root,bg="white", width=width, height=height )
        self.canvas.pack(fill=BOTH,expand=1)
        self.running = False
       
    
    def close(self):
        self.running = False
       
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def draw_line(self,line,fill_color):
        line.draw(self.canvas,fill_color)
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

class Line:
    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
    
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color)

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

