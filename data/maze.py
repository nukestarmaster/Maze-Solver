

import random
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
            delay = 0.001,
            seed = None
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
        if seed is not None:
            random.seed(seed)
        self._break_walls_r(random.randrange(self.num_columns), random.randrange(self.num_rows))
        self._reset_cells_visited()
    
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

    def _break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            switch = {'left': (i-1, j),
                      'right': (i+1, j),
                      'up': (i, j-1),
                      'down': (i, j+1)}
            to_visit = []
            for k in switch:
                if switch[k][0] in range(self.num_columns) and switch[k][1] in range(self.num_rows) and not self.cells[switch[k][0]][switch[k][1]].visited:
                    to_visit.append(k)
            if to_visit == []:
                return
            direction = to_visit[random.randrange(len(to_visit))]
            if direction == 'left':
                self.cells[i][j].left = False
                self.cells[i-1][j].right = False
            elif direction == 'right':
                self.cells[i][j].right = False
                self.cells[i+1][j].left = False
            elif direction == 'up':
                self.cells[i][j].top = False
                self.cells[i][j-1].bottom = False
            else:
                self.cells[i][j].bottom = False
                self.cells[i][j+1].top = False
            self.cells[i][j].draw("black")
            self._animate()
            self._break_walls_r(switch[direction][0], switch[direction][1])

    def _reset_cells_visited(self):
        for l in self.cells:
            for c in l:
                c.visited = False
    
    def solve(self):
        return self.solve_r(0, 0)
    
    def solve_r(self, i, j):
        self._animate()
        current_cell = self.cells[i][j]
        current_cell.visited = True
        if i == self.num_columns - 1 and j == self.num_rows - 1:
            return True
        switch = {'left': (i-1, j, current_cell.left),
                  'right': (i+1, j, current_cell.right),
                  'up': (i, j-1, current_cell.top),
                  'down': (i, j+1, current_cell.bottom)}
        for k in switch:
            if switch[k][0] in range(self.num_columns) and switch[k][1] in range(self.num_rows) and (not switch[k][2]) and (not self.cells[switch[k][0]][switch[k][1]].visited):
                current_cell.draw_move(self.cells[switch[k][0]][switch[k][1]])
                if self.solve_r(switch[k][0], switch[k][1]):
                    return True
                current_cell.draw_move(self.cells[switch[k][0]][switch[k][1]], True)
        return False