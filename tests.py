import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells1(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells2(self):
        num_cols = 50
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[len(m1._cells)//2]),
            num_rows,
        )

    def test_maze_create_cells3(self):
        num_cols = 16
        num_rows = 16
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[-1]),
            num_rows,
        )

    def test_break_entrance_and_exit1(self):
        num_cols = 16
        num_rows = 16
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        test = (m1._cells[0][0].has_top_wall, m1._cells[-1][-1].has_bottom_wall)
        expected = (False, False)
        self.assertEqual(test, expected)

    def test_break_entrance_and_exit2(self):
        num_cols = 25
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        test = (m1._cells[0][0].has_top_wall, m1._cells[-1][-1].has_bottom_wall)
        expected = (False, False)
        self.assertEqual(test, expected)

if __name__ == "__main__":
    unittest.main()
