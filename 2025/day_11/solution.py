from functools import cache
from pathlib import Path
from utils_anviks import parse_file_content, stopwatch

file = "data.txt"
file0 = "example.txt"
file_path = Path(__file__).parent / file
data = parse_file_content(file_path, ("\n", ": ", " "), str)
device_map = {k: v for (k,), v in data}


@stopwatch
def part1():
    @cache
    def count_paths_from(device: str) -> int:
        paths = 0

        for dest in device_map[device]:
            if dest == "out":
                paths += 1
            else:
                paths += count_paths_from(dest)

        return paths

    return count_paths_from("you")


@stopwatch
def part2():
    @cache
    def count_paths_from(device: str, seen_dac=False, seen_fft=False) -> int:
        paths = 0

        for dest in device_map[device]:
            if dest == "out":
                paths += seen_dac * seen_fft
            else:
                if dest == "fft":
                    seen_fft = True
                elif dest == "dac":
                    seen_dac = True
                paths += count_paths_from(dest, seen_dac, seen_fft)

        return paths

    return count_paths_from("svr")


if __name__ == "__main__":
    print(part1())  # 636               | 0.00005 seconds
    print(part2())  # 509312913844956   | 0.001 seconds
