from pathlib import Path
from utils_anviks import parse_file_content, stopwatch
from collections import deque

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ("\n", " "), str)


@stopwatch
def part1():
    total = 0

    for lights, *buttons, _ in data:
        lights = lights[1:-1]
        buttons = [eval(button[:-1] + "," + button[-1]) for button in buttons]
        queue = deque([(0, "." * len(lights), button, set()) for button in buttons])
        while queue:
            presses, state, next_button, seen = queue.popleft()
            new_state = list(state)
            for i in next_button:
                new_state[i] = [".", "#"][state[i] == "."]
            state = "".join(new_state)
            if state == lights:
                total += presses + 1
                break
            new_seen = seen | {next_button}
            for button in buttons:
                if button in new_seen:
                    continue  # Useless press
                queue.append((presses + 1, state, button, new_seen))

    return total


@stopwatch
def part2():
    pass


if __name__ == "__main__":
    print(part1())  # 473   | 14.84 seconds
    print(part2())
