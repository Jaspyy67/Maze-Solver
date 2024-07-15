from graphics import Line, Point


class Cell:
    def __init__(self, win = None
        ):

        self.has_left_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_top_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            left_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_line)
        else:
            left_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_line, fill_color = "white")
        if self.has_right_wall:
            right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_line)
        else:
            right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_line, fill_color = "white")
        if self.has_top_wall:
            top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_line)
        else:
            top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_line, fill_color = "white")
        if self.has_bottom_wall:
            bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_line)
        else:
            bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_line, fill_color = "white")

    def draw_move(self, to_cell, undo=False):
        current_location = Point((self._x1 + self._x2)/  2, (self._y1 + self._y2) / 2)
        target_location = Point((to_cell._x1 + to_cell._x2)/  2, (to_cell._y1 + to_cell._y2) / 2)
        
        fill_color = "gray" if undo else "red"
        self._win.draw_line(Line(current_location, target_location), fill_color)
