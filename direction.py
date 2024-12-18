from __future__ import annotations
from typing import Literal

Compass = Literal['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']


class Direction:
    __slots__ = ('row_delta', 'column_delta', '_direction')

    _DIRECTION_MAP: dict[Compass, tuple[int, int]] = {
        'N': (-1, 0),     # North
        'NE': (-1, 1),    # North-East
        'E': (0, 1),      # East
        'SE': (1, 1),     # South-East
        'S': (1, 0),      # South
        'SW': (1, -1),    # South-West
        'W': (0, -1),     # West
        'NW': (-1, -1)    # North-West
    }

    _ROTATION_ORDER = {
        'cardinal': ['N', 'E', 'S', 'W'],
        'diagonal': ['NE', 'SE', 'SW', 'NW'],
        'all': ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    }

    def __init__(self, direction: Compass):
        if direction not in self._DIRECTION_MAP:
            raise ValueError(f"Invalid direction: {direction}")
        self.row_delta, self.column_delta = self._DIRECTION_MAP[direction]
        self._direction = direction

    @property
    def name(self) -> str:
        return self._direction

    def rotate(self, steps: int, rotation_type: Literal['cardinal', 'diagonal', 'all'] = 'all') -> Direction:
        if rotation_type not in self._ROTATION_ORDER:
            raise ValueError(f"Invalid rotation type: {rotation_type}")

        rotation = self._ROTATION_ORDER[rotation_type]
        current_index = rotation.index(self._direction)
        new_index = (current_index + steps) % len(rotation)
        return Direction(rotation[new_index])

    def __neg__(self) -> Direction:
        """
        Get the opposite direction.

        :return: A new Direction instance pointing in the opposite direction.
        """
        opposite_delta = (-self.row_delta, -self.column_delta)
        for direction, delta in self._DIRECTION_MAP.items():
            if delta == opposite_delta:
                return Direction(direction)
        raise ValueError("Unable to find opposite direction.")

    def __eq__(self, other: Direction) -> bool:
        return self.row_delta == other.row_delta and self.column_delta == other.column_delta

    def __hash__(self) -> int:
        return hash((self.row_delta, self.column_delta))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self._direction}')"
