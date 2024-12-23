from collections import defaultdict

from utils_anviks import parse_file_content, stopwatch

file = 'data.txt'
file0 = 'example.txt'
data = parse_file_content(file, ('\n',), int)


def next_secret(n: int):
    n ^= n << 6 & 0xFFFFFF
    n ^= n >> 5 & 0xFFFFFF
    return n << 11 ^ n & 0xFFFFFF


@stopwatch
def solution():
    ans1 = 0
    ans2 = defaultdict(int)

    for i in range(len(data)):
        seen = set()
        secrets = [data[i]]
        for _ in range(2000):
            secrets.append(next_secret(secrets[-1]))
        ans1 += secrets[-1]

        diffs = [b % 10 - a % 10 for a, b in zip(secrets, secrets[1:])]

        for j in range(len(secrets) - 4):
            seq = tuple(diffs[j:j + 4])
            if seq not in seen:
                ans2[seq] += secrets[j + 4] % 10
                seen.add(seq)

    return ans1, max(ans2.values())


if __name__ == '__main__':
    print(*solution(), sep='\n')  # 19458130434, 2130   | 6.8 seconds
