from __future__ import annotations

import math
from collections import deque

from utils_anviks import read_file, stopwatch


class Module:
    def __init__(self, name: str, destinations: list[str]):
        self.name = name
        self.destinations = destinations

    def get_output(self, _input: bool, source: str) -> bool:
        return _input

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, destinations={self.destinations})"


class FlipFlop(Module):
    def __init__(self, name: str, destinations: list[str], on: bool = False):
        super().__init__(name, destinations)
        self.on = on

    def get_output(self, _input: bool, source: str) -> bool | None:
        if not _input:
            self.on = not self.on
            return self.on
        else:
            return None

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, on={self.on}, destinations={self.destinations})"


class Conjunction(Module):
    def __init__(self, name: str, destinations: list[str], inputs: dict[str, bool]):
        super().__init__(name, destinations)
        self.inputs = inputs

    def get_output(self, _input: bool, source: str) -> bool:
        self.inputs[source] = _input
        return not all(self.inputs.values())

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, destinations={self.destinations}, inputs={self.inputs})"


@read_file('data.txt', sep2=' -> ', auto_annotate=True)
@stopwatch
def solution(data: list[list[str]], part: int):
    modules = parse_modules(data)

    if part == 1:
        pulses = press_button(modules, 1000)
        return pulses['high'] * pulses['low']
    else:
        return find_minimum_pulses_needed(modules)


def parse_modules(data):
    """
    Parse the modules from the data.

    The modules are parsed into a dictionary, where the keys are the names of the modules and the values are the
    modules themselves. The modules are instances of the Module, FlipFlop, or Conjunction classes.
    :param data: The data to parse.
    :return: The parsed modules.
    """
    modules = {}

    for i in range(len(data)):
        name, destinations = data[i]
        destinations = destinations.split(', ')
        prefix = ''

        if name[0] in '%&':
            prefix, name = name[0], name[1:]
            data[i][0] = name

        if prefix == '%':
            module = FlipFlop(data[i][0], destinations)
        elif prefix == '&':
            module = Conjunction(data[i][0], destinations, {})
        else:
            module = Module(name, destinations)

        modules[name] = module

    # add inputs for conjunctions, because all the inputs' most recent pulses need to be tracked
    for module in modules.values():
        for dest in module.destinations:
            dest_mod = modules.get(dest)

            if isinstance(dest_mod, Conjunction):
                dest_mod.inputs[module.name] = False

    return modules


def press_button(modules, times: int) -> dict[str, int]:
    """
    Press the button a given number of times and return the number of high and low pulses sent.
    :param modules: The modules.
    :param times: The number of times to press the button.
    :return: The number of high and low pulses sent.
    """
    pulses = {'low': 0, 'high': 0}

    for _ in range(times):
        pulses['low'] += 1
        # module, pending output
        queue = deque([(modules['broadcaster'], False)])

        while queue:
            src_module, pulse = queue.popleft()
            # print(src_module, pulse)

            for dest_name in src_module.destinations:
                # print(src_module.name, f"-{'high' if pulse else 'low'}->", dest_name)
                pulses['high' if pulse else 'low'] += 1

                dest_module = modules.get(dest_name)
                if dest_module is None:
                    continue

                out_pulse = dest_module.get_output(pulse, src_module.name)
                if out_pulse is not None:
                    queue.append((dest_module, out_pulse))

    return pulses


def find_minimum_pulses_needed(modules) -> int:
    """
    Find the minimum number of button presses needed for module 'rx' to receive one low pulse.

    The number of button presses needed for module 'rx' to receive one low pulse is the least common multiple of the
    4 chains of flip-flops and conjunctions that lead to 'rx'. Each chain is represented as a binary number, where each
    bit is a flip-flop that links to a conjunction (1) or not (0). Flip-flops that link to a conjunction are ones,
    because they need to send a high pulse to it in order for the conjunction to send a low pulse to the
    next modules. Everything else is a zero, because they don't need to send a high pulse to the next modules.

    Visualization of the chains: https://www.reddit.com/media?url=https%3A%2F%2Fi.redd.it%2Fehu8t3oy5e7c1.png
    Credit: https://www.reddit.com/r/adventofcode/comments/18mmfxb/comment/ke5sgxs/
    :param modules: The modules.
    :return: The minimum number of button presses needed for module 'rx' to receive one low pulse.
    """
    chain_values = []
    for chain_start in modules['broadcaster'].destinations:
        next_flipflop = [chain_start]
        binary_chain = 0
        pos = 0

        while next_flipflop:
            flipflop = modules[next_flipflop[0]]
            destinations = flipflop.destinations

            # all flip-flops have 1-2 targets
            # there are no flip-flops with 2 targets of the same type
            # flip-flops that link to a conjunction are ones, everything else is a zero
            binary_chain |= (len(destinations) == 2 or isinstance(modules[destinations[0]], Conjunction)) << pos
            pos += 1
            next_flipflop = [dest for dest in destinations if isinstance(modules[dest], FlipFlop)]

        chain_values.append(binary_chain)

    return math.lcm(*chain_values)


if __name__ == '__main__':
    print(solution(1))  # 866435264
    print(solution(2))  # 229215609826339
