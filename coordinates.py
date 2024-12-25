from typing import Any, Generator, Literal


class Cell:
    __slots__ = ('row', 'column')

    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column

    @property
    def up(self):
        return Cell(self.row - 1, self.column)

    @property
    def down(self):
        return Cell(self.row + 1, self.column)

    @property
    def left(self):
        return Cell(self.row, self.column - 1)

    @property
    def right(self):
        return Cell(self.row, self.column + 1)

    def neighbours(self, nb_type: Literal['cardinal', 'diagonal', 'all']) -> Generator['Cell', Any, None]:
        for nb in self.neighbour_directions(nb_type):
            yield self + nb

    @staticmethod
    def neighbour_directions(nb_type: Literal['cardinal', 'diagonal', 'all']) -> tuple[tuple[int, int], ...]:
        if nb_type == 'cardinal':
            neighbours = ((0, 1), (1, 0), (0, -1), (-1, 0))
        elif nb_type == 'diagonal':
            neighbours = ((1, 1), (1, -1), (-1, -1), (-1, 1))
        elif nb_type == 'all':
            neighbours = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1))
        else:
            raise ValueError(f'Invalid neighbour type: {nb_type}')

        return neighbours

    def manhattan_distance(self, other: 'Cell') -> int:
        """
        Return the Manhattan distance between two cells.

        The Manhattan distance is the sum of the absolute differences between the row and column coordinates.
        In other words, it is the distance between two points if you could only move in cardinal directions.
        ::
                  -2  -1   0   1   2
                -----------------------
            -2  |  4   3   2   3   4  |
            -1  |  3   2   1   2   3  |
             0  |  2   1   X   1   2  |
             1  |  3   2   1   2   3  |
             2  |  4   3   2   3   4  |
                -----------------------

        :param other: The other cell.
        :return: The Manhattan distance between the two cells.
        """
        return abs(self.row - other.row) + abs(self.column - other.column)

    def euclidean_distance(self, other: 'Cell') -> float:
        """
        Return the Euclidean distance between two cells.

        The Euclidean distance is the straight-line distance between two points.
        ::
                    -2  -1   0   1   2
                -----------------------
            -2  |  2.8 2.2 2.0 2.2 2.8 |
            -1  |  2.2 1.4 1.0 1.4 2.2 |
             0  |  2.0 1.0  X  1.0 2.0 |
             1  |  2.2 1.4 1.0 1.4 2.2 |
             2  |  2.8 2.2 2.0 2.2 2.8 |
                -----------------------

        :param other: The other cell.
        :return: The Euclidean distance between the two cells.
        """
        return ((self.row - other.row) ** 2 + (self.column - other.column) ** 2) ** 0.5

    def chebyshev_distance(self, other: 'Cell') -> int:
        """
        Return the Chebyshev distance between two cells.

        The Chebyshev distance is the maximum of the absolute differences between the row and column coordinates.
        In other words, it is the distance between two points if you could move in cardinal and diagonal directions.
        ::
                  -2  -1   0   1   2
                -----------------------
            -2  |  2   2   2   2   2  |
            -1  |  2   1   1   1   2  |
             0  |  2   1   X   1   2  |
             1  |  2   1   1   1   2  |
             2  |  2   2   2   2   2  |
                -----------------------

        :param other: The other cell.
        :return: The Chebyshev distance between the two cells.
        """
        return max(abs(self.row - other.row), abs(self.column - other.column))

    def is_neighbour(self, other: 'Cell', nb_type: Literal['cardinal', 'diagonal', 'all']) -> bool:
        """
        Check if the other cell is a neighbour of this cell.

        :param other: The other cell.
        :param nb_type: The type of neighbours to consider.
        :return: True if the other cell is a neighbour, False otherwise.
        """
        if nb_type == 'cardinal':
            return abs(self.row - other.row) + abs(self.column - other.column) == 1
        elif nb_type == 'diagonal':
            return abs(self.row - other.row) == 1 and abs(self.column - other.column) == 1
        elif nb_type == 'all':
            return abs(self.row - other.row) <= 1 and abs(self.column - other.column) <= 1 and self != other

    def line_of_sight(self, other: 'Cell', can_move_diagonally: bool = False) -> Generator['Cell', Any, None]:
        """
        Generate all cells along the line of sight to another Cell (inclusive).
        """
        d_row = other.row - self.row
        d_col = other.column - self.column
        steps = max(abs(d_row), abs(d_col))
        if can_move_diagonally:
            for i in range(steps + 1):
                yield Cell(self.row + (i * d_row // steps), self.column + (i * d_col // steps))
        else:
            # TODO: Should this exist?
            # Cardinal-only movement: row-first, then column
            current_row, current_col = self.row, self.column

            # Move along rows first
            row_step = 1 if d_row > 0 else -1
            for _ in range(abs(d_row)):
                current_row += row_step
                yield Cell(current_row, current_col)

            # Then move along columns
            col_step = 1 if d_col > 0 else -1
            for _ in range(abs(d_col)):
                current_col += col_step
                yield Cell(current_row, current_col)

    def _operate(self, other, op):
        if isinstance(other, Cell):
            return Cell(op(self.row, other.row), op(self.column, other.column))
        elif isinstance(other, tuple):
            if len(other) == 2:
                return Cell(op(self.row, other[0]), op(self.column, other[1]))
            raise ValueError("Tuple must have exactly two elements")
        elif isinstance(other, int):
            return Cell(op(self.row, other), self.column)
        elif isinstance(other, complex):
            return Cell(op(self.row, int(other.real)), op(self.column, int(other.imag)))
        return NotImplemented

    def __add__(self, other):
        return self._operate(other, lambda x, y: x + y)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self._operate(other, lambda x, y: x - y)

    def __rsub__(self, other):
        return self - other

    def __complex__(self):
        return complex(self.row, self.column)

    def __iter__(self):
        yield self.row
        yield self.column

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __lt__(self, other):
        return self.row >= other.row

    def __gt__(self, other):
        return self.row <= other.row

    def __hash__(self):
        return hash((self.row, self.column))

    def __repr__(self):
        return f"{self.__class__.__name__}(row={self.row}, column={self.column})"
