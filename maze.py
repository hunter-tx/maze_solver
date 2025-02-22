from pydoc_data.topics import topics

from graphics import *
import time
import random

class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None,
                 seed=None
                 ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            row_list = []
            for j in range(self._num_rows):
                row_list.append(Cell(self._win))
            self._cells.append(row_list)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        curr_cell = self._cells[i][j]
        x1 = (self._cell_size_x * i) + self._x1
        x2 = (self._cell_size_x * (i + 1)) + self._x1
        y1 = (self._cell_size_y * j) + self._y1
        y2 = (self._cell_size_y * (j + 1)) + self._y1
        curr_cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            if self._is_within_bounds(i - 1, j):
                if not self._cells[i-1][j].visited:
                    to_visit.append((i - 1, j))
            if self._is_within_bounds(i, j - 1):
                if not self._cells[i][j -1 ].visited:
                    to_visit.append((i, j - 1))
            if self._is_within_bounds(i + 1, j):
                if not self._cells[i + 1][j].visited:
                    to_visit.append((i + 1, j))
            if self._is_within_bounds(i, j + 1):
                if not self._cells[i][j + 1].visited:
                    to_visit.append((i, j + 1))
            if not to_visit:
                self._draw_cell(i, j)
                return
            if len(to_visit) > 1:
                move_to_index = random.randrange(0, len(to_visit))
            else:
                move_to_index = 0
            to_visit_cell = self._cells[to_visit[move_to_index][0]][to_visit[move_to_index][1]]
            dx = to_visit[move_to_index][0] - i
            dy = to_visit[move_to_index][1] - j
            self._knock_down_wall(current_cell, to_visit_cell, dx, dy)
            self._break_walls_r(to_visit[move_to_index][0], to_visit[move_to_index][1])

    def _is_within_bounds(self, i, j):
        return 0 <= i < self._num_cols and 0 <= j < self._num_rows

    def _knock_down_wall(self, current_cell, next_cell, dx, dy):
        if dx == -1:  # Moving left
            current_cell.has_left_wall = False
            next_cell.has_right_wall = False
        elif dx == 1:  # Moving right
            current_cell.has_right_wall = False
            next_cell.has_left_wall = False
        elif dy == -1:  # Moving up
            current_cell.has_top_wall = False
            next_cell.has_bottom_wall = False
        elif dy == 1:  # Moving down
            current_cell.has_bottom_wall = False
            next_cell.has_top_wall = False

    def _reset_cells_visited(self):
        for column in self._cells:
            for row in column:
                row.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self,i, j):
        curr_cell = self._cells[i][j]
        self._animate()
        curr_cell.visited = True
        if curr_cell == self._cells[-1][-1]:
            return True
        if self._is_within_bounds(i, j - 1): # top_cell
            top_cell = self._cells[i][j - 1]
            if not curr_cell.has_top_wall and not top_cell.visited:
                curr_cell.draw_move(top_cell)
                if self._solve_r(i, j - 1):
                    return True
                top_cell.draw_move(curr_cell, undo=True)
        if self._is_within_bounds(i + 1, j): # right_cell
            right_cell = self._cells[i + 1][j]
            if not curr_cell.has_right_wall and not right_cell.visited:
                curr_cell.draw_move(right_cell)
                if self._solve_r(i + 1, j):
                    return True
                right_cell.draw_move(curr_cell, undo=True)
        if self._is_within_bounds(i, j + 1): # bottom_cell
            bottom_cell = self._cells[i][j + 1]
            if not curr_cell.has_bottom_wall and not bottom_cell.visited:
                curr_cell.draw_move(bottom_cell)
                if self._solve_r(i, j + 1):
                    return True
                bottom_cell.draw_move(curr_cell, undo=True)
        if self._is_within_bounds(i - 1, j): # left_cell
            left_cell = self._cells[i - 1][j]
            if not curr_cell.has_left_wall and not left_cell.visited:
                curr_cell.draw_move(left_cell)
                if self._solve_r(i - 1, j):
                    return True
                left_cell.draw_move(curr_cell, undo=True)
        return False

