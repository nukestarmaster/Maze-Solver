from tkinter import Tk, BOTH, Canvas

class window:
    def __init__(self, width, length):
        self.root_widget = Tk()
        self.root_widget.title = "maze_solver"
        self.canvas = Canvas()
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