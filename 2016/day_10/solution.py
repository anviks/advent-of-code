from collections import defaultdict
from pathlib import Path
import re
from utils_anviks import parse_file_content, stopwatch
from more_itertools import partition

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ("\n",), str)
initial, trades = partition(lambda s: s.startswith("bot"), data)


@stopwatch
def solve():
    bots: defaultdict[str, list[int]] = defaultdict(list)
    outputs: defaultdict[str, list[int]] = defaultdict(list)
    dest = {"bot": bots, "output": outputs}

    for init in initial:
        value, bot = re.findall(r"\d+", init)
        bots[bot].append(int(value))

    trade_dict = {}

    for trade in trades:
        trader = r"(bot|output) (\d+)"
        src, low_t, low_n, high_t, high_n = re.search(rf"(\d+).*{trader}.*{trader}", trade).groups()  # type: ignore
        trade_dict[src] = (low_t, low_n, high_t, high_n)

    result_bot = None

    while True:
        ready = [bot for bot, chips in bots.items() if len(chips) == 2]
        if not ready:
            break

        for bot in ready:
            chips = sorted(bots.pop(bot))
            low, high = chips

            if chips == [17, 61]:
                result_bot = int(bot)

            low_t, low_n, high_t, high_n = trade_dict[bot]

            dest[low_t][low_n].append(low)
            dest[high_t][high_n].append(high)

            if result_bot is not None and outputs.keys() & set("012") == set("012"):
                return result_bot, outputs["0"][0] * outputs["1"][0] * outputs["2"][0]


if __name__ == "__main__":
    print(solve())  # 141, 1209 | 0.00093 seconds
