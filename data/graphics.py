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
                 left_wall = True,
                 right_wall = True,
                 top_wall = True,
                 bottom_wall = True):
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.win = win
    
    def draw(self, fill):
        if self.top_wall:
            self.win.draw_line(line(point(self.x1, self.y1),
                                    point(self.x2, self.y1)),
                               fill)
        if self.bottom_wall:
            self.win.draw_line(line(point(self.x1, self.y2),
                                    point(self.x2, self.y2)),
                               fill)
        if self.left_wall:
            self.win.draw_line(line(point(self.x1, self.y1),
                                    point(self.x1, self.y2)),
                               fill)
        if self.right_wall:
            self.win.draw_line(line(point(self.x2, self.y1),
                                    point(self.x2, self.y2)),
                               fill)
            
    def centre(self):
        return point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
            

    def draw_move(self, to_cell, undo = False):
        colour = "red"
        if undo:
            colour = "gray"
        line1 = line(self.centre(), to_cell.centre())
        line1.draw(self.win.canvas, colour)

class maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_columns,
            cell_width,
            cell_height,
            win
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.win = win
        self.cells = []
    
    def _create_cells(self):
        for i in range(self.num_columns):
            list = []
            for j in range(self.num_rows):
                list.append(cell(
                    self.x1 + i * self.cell_width,
                    self.x1 + (i + 1) * self.cell_width,
                    self.y1 + j * self.cell_height,
                    self.y1 + (j + 1) * self.cell_height,
                    self.win))
            self.cells.append(list)
        for l in self.cells:
            for c in l:
                c.draw("black")
        self._animate()

    def _animate(self):
        self.win.redraw()
        sleep(0.05)