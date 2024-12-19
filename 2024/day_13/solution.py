import re

import numpy as np
from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n\n', '\n'), str)
data = [[tuple(map(int, re.search(r': X[+=](\d+), Y[+=](\d+)', s).groups())) for s in seq] for seq in data]


@stopwatch
def solve(part: int):
    """
    Solve the problem using linear algebra.
    Input data of
    Button A: X+79, Y+87
    Button B: X+44, Y+14
    Prize: X=7384, Y=4824
    becomes a matrix equation and is solved using numpy.linalg.solve.
    The matrix equation is:
    [79 44] [x] = [7384]
    [87 14] [y]   [4824]
    """
    tokens = 0
    for a, b, prize in data:
        button_movement = np.array([*zip(a, b)])  # [[79 44], [87 14]]
        prize_vector = np.array(prize) + (part == 2) * 10000000000000  # [7384 4824]
        button_presses = np.round(np.linalg.solve(button_movement, prize_vector))  # [40. 96.] - button A is pressed 40 times, button B is pressed 96 times
        if (button_presses @ button_movement.transpose() == prize_vector).all():  # Multiply button presses by button movement and check if it indeed reaches the prize
            tokens += int(button_presses @ (3, 1))  # Multiply button presses by their costs and add to tokens
    return tokens


if __name__ == '__main__':
    print(solve(1))  # 26299               | 0.007 seconds
    print(solve(2))  # 107824497933339     | 0.007 seconds
