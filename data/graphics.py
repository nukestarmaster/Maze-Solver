from time import sleep
from tkinter import Tk, BOTH, Canvas

class window:
    def __init__(self, width, length):
        self.root_widget = Tk()
        self.root_widget.title = "maze_solver"
        self.canvas = Canvas(width= width, height= length)
        self.canvas.pack()
        self.running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close())

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Window Closed")
    
    def close(self):
        self.running = False
    
    def draw_line(self, line, fill_colour):
        line.draw(self.canvas, fill_colour)

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class line:
    def __init__(self, a, b):
        self.a = a
        self.b = b
     
    def draw(self, canvas, fill_colour):
        canvas.create_line(
            self.a.x,
            self.a.y,
            self.b.x,
            self.b.y,
            fill = fill_colour,
            width = 2
        )
        canvas.pack()

class cell:
    def __init__(self,
                 x1,
                 x2,
                 y1,
                 y2,
                 win,
                 left = True,
                 right = True,
                 top = True,
                 bottom = True):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.win = win
        self.left_wall = line(point(self.x1, self.y1), point(self.x1, self.y2))
        self.right_wall = line(point(self.x2, self.y1), point(self.x2, self.y2))
        self.top_wall = line(point(self.x1, self.y1), point(self.x2, self.y1))
        self.bottom_wall = line(point(self.x1, self.y2), point(self.x2, self.y2))
    
    def draw(self, fill):
        if self.win is None:
            return
        self.draw_helper(fill, self.left, self.left_wall)
        self.draw_helper(fill, self.right, self.right_wall)
        self.draw_helper(fill, self.top, self.top_wall)
        self.draw_helper(fill, self.bottom, self.bottom_wall)

    def draw_helper(self, fill, side_bool, side):
        if side_bool:
            self.win.draw_line(side, fill)
        else:
            self.win.draw_line(side, "white")
            

            
    def centre(self):
        return point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
            

    def draw_move(self, to_cell, undo = False):
        colour = "red"
        if undo:
            colour = "gray"
        line1 = line(self.centre(), to_cell.centre())
        line1.draw(self.win.canvas, colour)