from data.graphics import window, line, point

width = 800
height = 600

line1 = line(point(0,0), point(width, height))


def main():
    win = window(width, height)
    win.draw_line(line1, "red")
    win.wait_for_close()

main()