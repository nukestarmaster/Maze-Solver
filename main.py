from data.graphics import window
from data.maze import maze

border = 15
cell_width = 25
cell_height = 25
columns = 20
rows = 20
delay = 0.01




def main():
    win = window(2 * border + cell_width * columns, 2 * border + cell_height * rows)
    maze1 = maze(border, border, columns, rows, cell_width, cell_height, win, delay)
    win.wait_for_close()

main()