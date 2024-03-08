import math
import re
from typing import Callable

from utils_anviks import read_file, stopwatch


class Predicate:
    def __init__(self, arg_operand: str, operation: Callable, fixed_operand: int):
        self.arg_operand = arg_operand
        self.operation = operation
        self.fixed_operand = fixed_operand

    def evaluate(self, values: dict) -> bool:
        return self.operation(values.get(self.arg_operand), self.fixed_operand)

    def __bool__(self) -> bool:
        return False

    def __repr__(self):
        return f"Predicate({self.arg_operand}, {self.operation}, {self.fixed_operand})"


@read_file('data.txt', sep='\n\n', sep2='\n', auto_annotate=True)
@stopwatch
def solution(data: list[list[str]], part: int):
    flows = data[0]
    rules = {}

    for f in flows:
        name, flow = re.search(r"(\w{1,3}){(.*(?=}))", f).groups()
        rules[name] = []

        for instruction in flow.split(','):
            rule = []
            instruction = instruction.split(':')
            result = instruction[-1]
            predicate = instruction[0]

            if result == predicate:
                predicate = True
            else:
                func = int.__gt__ if predicate[1] == '>' else int.__lt__
                predicate = Predicate(predicate[0], func, int(predicate[2:]))

            rule.append(predicate)
            rule.append(result)

            rules[name].append(rule)

    if part == 1:
        ratings = []
        for i in range(len(data[1])):
            ratings.append(eval('dict(' + data[1][i][1:-1] + ')'))
        return part_1(ratings, rules)
    else:
        ranges = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
        return part_2(ranges, rules)


def part_1(ratings, rules):
    acc = 0
    break_flag = False

    for r in ratings:
        current_rule = rules['in']
        while True:
            for condition, result in current_rule:
                if condition or condition.evaluate(r):
                    if result in rules:
                        current_rule = rules[result]
                        break
                    elif result == 'A':
                        acc += sum(r.values())

                    break_flag = True
                    break

            if break_flag:
                break_flag = False
                break

    return acc


def part_2(ranges, rules, rule_name='in'):
    if all(_range[0] - _range[1] > 0 for _range in ranges.values()):
        return 0

    acc = 0

    if rule_name == 'A':
        return math.prod(_range[1] - _range[0] + 1 for _range in ranges.values())
    elif rule_name == 'R':
        return 0

    rule = rules[rule_name]

    for instruction in rule:
        condition, result = instruction

        if isinstance(condition, Predicate):
            split_value = condition.fixed_operand
            rule_name = condition.arg_operand
            current_min, current_max = ranges[rule_name]
            copy_ranges = ranges.copy()

            if condition.operation == int.__lt__:
                if current_max < split_value:
                    acc += part_2(copy_ranges, rules, result)
                else:
                    copy_ranges[rule_name] = current_min, split_value - 1
                    acc += part_2(copy_ranges, rules, result)
                    ranges[rule_name] = split_value, current_max
            else:
                if current_min > split_value:
                    acc += part_2(copy_ranges, rules, result)
                else:
                    copy_ranges[rule_name] = split_value + 1, current_max
                    acc += part_2(copy_ranges, rules, result)
                    ranges[rule_name] = current_min, split_value

        elif condition:
            acc += part_2(ranges.copy(), rules, result)

    return acc


if __name__ == '__main__':
    f = solution(1)
    print(f)  # 377025
    print(f == 377025)

    g = solution(2)
    print(g)  # 135506683246673  |  0.0045s
    print(g == 135506683246673)
