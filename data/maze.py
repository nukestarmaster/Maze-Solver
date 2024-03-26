

import time
from data.graphics import cell


class maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_columns,
            cell_width,
            cell_height,
            win = False,
            delay = 0.001
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.win = win
        self.delay = delay
        self.cells = []
        self._create_cells()
        self._break_entrance_and_exit()
    
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
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(self.delay)

    def _break_entrance_and_exit(self):
        self.cells[0][0].left = False
        self.cells[0][0].draw("black")
        self._animate()
        self.cells[-1][-1].right = False
        self.cells[-1][-1].draw("black")
        self._animate()