from itertools import chain, combinations, combinations_with_replacement, product
from pathlib import Path
from line_profiler import profile
from more_itertools import collapse, flatten
from utils_anviks import parse_file_content, stopwatch
from heapq import heappush, heappop
from collections import Counter, defaultdict, deque

file = 'data.txt'
file0 = 'example.txt'
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ('\n', ' '), str)


@stopwatch
# @profile
def part1():
    total = 0
    loops = 0

    for lights, *buttons, _ in data:
        lights = lights[1:-1]
        buttons = [eval(button[:-1] + ',' + button[-1]) for button in buttons]
        queue = deque([(0, '.' * len(lights), button, set()) for button in buttons])
        while queue:
            presses, state, next_button, seen = queue.popleft()
            new_state = list(state)
            for i in next_button:
                new_state[i] = ['.', '#'][state[i] == '.']
            state = ''.join(new_state)
            if state == lights:
                total += presses + 1
                break
            new_seen = seen | {next_button}
            for button in buttons:
                if button in new_seen:
                    continue  # Useless press
                queue.append((presses + 1, state, button, new_seen))

        loops += 1
        print('loop', loops)
        # if total > 150:
        #     break

    return total


# @stopwatch
# def part2():
#     total = 0
#     loops = 0

#     for _, *buttons, joltage in data:
#         joltage = eval(joltage[1:-1])
#         buttons = [eval(button[:-1] + ',' + button[-1]) for button in buttons]
#         queue = deque([(0, (0,) * len(joltage), button) for button in buttons])
#         while queue:
#             presses, state, next_button = queue.popleft()
#             new_state = list(state)
#             for i in next_button:
#                 new_state[i] += 1
#                 if new_state[i] > joltage[i]:
#                     break
#             else:
#                 state = tuple(new_state)
#                 if state == joltage:
#                     total += presses + 1
#                     break
#                 for button in buttons:
#                     queue.append((presses + 1, state, button))

#         loops += 1
#         print('loop', loops)
#         # if total > 150:
#         #     break

#     return total


# @stopwatch
# def part2():
#     total = 0

#     for _, *buttons, joltage in data:
#         joltage = eval(joltage[1:-1])
#         buttons = [eval(button[:-1] + ',' + button[-1]) for button in buttons]
#         print(buttons, joltage)

#         d = defaultdict(list)

#         for i, jolt in enumerate(joltage):
#             for button in buttons:
#                 if i in button:
#                     d[jolt].append(button)
        
#         print(d)
#         results = []

#         for times, options in d.items():
#             results.append(list(combinations_with_replacement(options, times)))

#         # print(*results, sep='\n')

#         for smth in product(*results):
#             counter = Counter(collapse(smth))
#             res = tuple(v for _, v in sorted(counter.items()))
#             if res == joltage:
#                 print('letsgo?')
#             # break

#         break




# @stopwatch
# def part2():
#     total = 0
#     loops = 0

#     for _, *buttons, target in data:
#         target = eval(target[1:-1])
#         start = (0,) * len(target)
#         buttons = [eval(button[:-1] + ',' + button[-1]) for button in buttons]
        
#         queue = deque([(start, 0)])
#         visited = {start}

#         while queue:
#             state, presses = queue.popleft()

#             if state == target:
#                 total += presses
#                 print(presses)
#                 break

#             for button in buttons:
#                 new_state = list(state)
#                 for i in button:
#                     new_state[i] += 1
#                     if new_state[i] > target[i]:
#                         break
#                 else:
#                     new_state = tuple(new_state)

#                     if new_state in visited:
#                         continue

#                     visited.add(new_state)

#                     queue.append((new_state, presses + 1))

#         loops += 1
#         print('loop', loops)

#     return total



from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

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
    result = milp(c=c, constraints=constraints, bounds=bounds, integrality=np.ones(n_buttons))

    return int(result.fun)


@stopwatch
def part2():
    total = 0

    for _, *buttons, target in data:
        target = eval(target[1:-1])
        buttons = [eval(button[:-1] + ',' + button[-1]) for button in buttons]
        total += min_button_presses_ilp(buttons, target)

    return total


if __name__ == '__main__':
    # print(part1())  # 473   | 14.84 seconds
    print(part2())  # 18681 | 0.25 seconds
