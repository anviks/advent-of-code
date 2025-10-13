from collections import defaultdict
from pathlib import Path
import re
from utils_anviks import parse_file_content, stopwatch
from more_itertools import partition

file = "data.txt"
file0 = "example.txt"
file_path = str(Path(__file__).parent / file)
data = parse_file_content(file_path, ("\n",), str)
initial, trades = partition(lambda s: s.startswith("bot"), data)


@stopwatch
def solve():
    bots: defaultdict[str, list[int]] = defaultdict(list)
    outputs = {}

    for init in initial:
        value, bot = re.findall(r"\d+", init)
        bots[bot].append(int(value))

    trade_dict = {}

    for trade in trades:
        trader = r"(bot|output) (\d+)"
        source_bot, low_type, low_num, high_type, high_num = re.search(rf"(\d+).*{trader}.*{trader}", trade).groups()  # type: ignore
        trade_dict[source_bot] = (low_type, low_num, high_type, high_num)

    result_bot = -1

    while True:
        for source_bot, chips in bots.copy().items():
            if len(chips) == 2:
                chips.sort()
                if chips == [17, 61]:
                    result_bot = int(source_bot)
                low_type, low_num, high_type, high_num = trade_dict[source_bot]

                low = chips.pop(0)
                if low_type == "bot":
                    bots[low_num].append(low)
                else:
                    outputs[low_num] = low

                high = chips.pop(0)
                if high_type == "bot":
                    bots[high_num].append(high)
                else:
                    outputs[high_num] = high

                if result_bot >= 0 and outputs.keys() & set("012") == set("012"):
                    return result_bot, outputs["0"] * outputs["1"] * outputs["2"]


if __name__ == "__main__":
    print(solve())  # 141, 1209 | 0.00093 seconds
