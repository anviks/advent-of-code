from pathlib import Path
from utils_anviks import parse_file_content, stopwatch
from collections import deque
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np


file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ("\n", " "), str)


def get_min_presses(buttons, lights):
    queue = deque([(0, "." * len(lights), button, set()) for button in buttons])

    while queue:
        presses, state, next_button, seen = queue.popleft()

        new_state = list(state)
        for i in next_button:
            new_state[i] = [".", "#"][state[i] == "."]
        state = "".join(new_state)

        if state == lights:
            return presses + 1

        new_seen = seen | {next_button}

        for button in buttons:
            if button in new_seen:
                continue  # Useless press
            queue.append((presses + 1, state, button, new_seen))

    return 0


@stopwatch
def part1():
    total = 0

    for lights, *buttons, _ in data:
        lights = lights[1:-1]
        buttons = tuple([eval(button[:-1] + "," + button[-1]) for button in buttons])
        total += get_min_presses(buttons, lights)

    return total


def min_button_presses_ilp(buttons, target):
    """
    Formulate as Integer Linear Programming problem.
    Find minimum sum of button presses.

    PS: Written by Claude (claude.ai), because wtf is this?
    """
    n_buttons = len(buttons)
    n_positions = len(target)

    # Create constraint matrix: each column is a button, each row is a position
    A = np.zeros((n_positions, n_buttons))
    for j, button in enumerate(buttons):
        for pos in button:
            A[pos, j] = 1

    # Objective: minimize sum of all button presses
    c = np.ones(n_buttons)

    # Constraints: A @ x == target (each position must reach its target value)
    constraints = LinearConstraint(A, target, target)

    # Bounds: each button can be pressed 0 to max(target) times
    bounds = Bounds(0, max(target))

    # Solve as integer program
    result = milp(
        c=c, constraints=constraints, bounds=bounds, integrality=np.ones(n_buttons)
    )

    return int(result.fun)


@stopwatch
def part2():
    total = 0

    for _, *buttons, target in data:
        target = eval(target[1:-1])
        buttons = [eval(button[:-1] + "," + button[-1]) for button in buttons]
        total += min_button_presses_ilp(buttons, target)

    return total


if __name__ == "__main__":
    print(part1())  # 473   | 14.84 seconds
    print(part2())  # 18681 | 0.25 seconds
