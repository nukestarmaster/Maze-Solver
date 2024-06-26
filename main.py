from data.graphics import window
from data.maze import maze

border = 15
cell_width = 25
cell_height = 25
columns = 25
rows = 25
delay = 0.01




def main():
    win = window(2 * border + cell_width * columns, 2 * border + cell_height * rows)
    maze1 = maze(border, border, columns, rows, cell_width, cell_height, win, delay)
    maze1.solve()
    win.wait_for_close()

main()