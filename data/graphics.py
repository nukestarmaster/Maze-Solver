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
        self._create_cells()
        self._break_entrance_and_exit()
        self._animate()
    
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

    def _animate(self):
        self.win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self.cells[0][0].left_wall = False
        self.cells[-1][-1].right_wall = False