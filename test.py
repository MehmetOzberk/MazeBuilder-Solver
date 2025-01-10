import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        win = Window(800, 600)
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10,win,seed=10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )
    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        win = Window(800, 600)
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10,win,seed=10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        win = Window(800, 600)
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10,win, seed=10)
        for col in m1.cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )


if __name__ == "__main__":
    unittest.main()