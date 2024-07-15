from cells import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None
        ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed
        self._create_cells()
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

  


    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range (self._num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)


    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = []
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                possible_directions.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                possible_directions.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                possible_directions.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                possible_directions.append((i, j + 1))

            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return
            direction_index = random.randrange(len(possible_directions))
            next_index = possible_directions[direction_index]
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False


    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        current_cell = self._cells[i][j]
        self._animate()
        if current_cell == self._cells[self._num_cols - 1][self._num_rows - 1]:
            return True
        self._cells[i][j].visited = True
        possible_cell = []
        #left
        if i > 0 and not self._cells[i - 1][j].visited and self._cells[i][j].has_left_wall == False:
            possible_cell.append((i - 1,j))
        # right
        if i < self._num_cols - 1 and not self._cells[i + 1][j].visited and self._cells[i][j].has_right_wall == False:
            possible_cell.append((i + 1, j))
        # up
        if j > 0 and not self._cells[i][j - 1].visited and self._cells[i][j].has_top_wall == False:
            possible_cell.append((i,j - 1))
         # down
        if j < self._num_rows - 1 and not self._cells[i][j + 1].visited and self._cells[i][j].has_bottom_wall == False:
            possible_cell.append((i, j + 1))

        for ni, nj in possible_cell:
            next_cell = self._cells[ni][nj]
            current_cell.draw_move(next_cell)
            if self._solve_r(ni, nj):
                return True
            current_cell.draw_move(next_cell, undo=True)
        self._animate()
        return False

    





