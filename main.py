from data.graphics import window, maze

border = 15
cell_width = 10
cell_height = 10
columns = 100
rows = 100




def main():
    win = window(2 * border + cell_width * columns, 2 * border + cell_height * rows)
    maze1 = maze(border, border, columns, rows, cell_width, cell_height, win)
    win.wait_for_close()

main()