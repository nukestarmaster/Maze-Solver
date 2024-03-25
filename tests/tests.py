import sys
sys.path.append(r"/home/nukestar/workspace/Maze-Solver/")
import unittest
from data.graphics import maze, window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        win = window(100, 100)
        m1 = maze(0, 0, num_rows, num_cols, 10, 10, win)
        print(m1.cells)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

if __name__ == "__main__":
    unittest.main()

