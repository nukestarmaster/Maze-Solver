from data.graphics import window, line, point, cell

width = 800
height = 600




def main():
    win = window(width, height)
    cell1 = cell(20, 50, 20, 50, win)
    cell2 = cell(80, 90, 80, 90, win)
    cell1.top_wall = False
    cell1.draw("red")
    cell2.draw("blue")
    cell1.draw_move(cell2, False)
    win.wait_for_close()

main()