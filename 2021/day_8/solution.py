import time

from utils_anviks import read_file


def __get_segments(display: list[str]):
    segments = [""] * 10
    segments[1] = min(display, key=len)
    display.remove(segments[1])
    segments[7] = min(display, key=len)
    display.remove(segments[7])
    segments[4] = min(display, key=len)
    display.remove(segments[4])
    segments[8] = max(display, key=len)
    display.remove(segments[8])

    n2_3_5 = {seg for seg in display if len(seg) == 5}
    n0_6_9 = {seg for seg in display if len(seg) == 6}

    for num in n0_6_9:
        for seg in segments[4]:
            if seg not in num:
                break
        else:
            segments[9] = num
            n0_6_9.remove(num)
            break

    for num in n0_6_9:
        for seg in segments[1]:
            if seg not in num:
                break
        else:
            segments[0] = num
            n0_6_9.remove(num)
            segments[6] = n0_6_9.pop()
            break


    for num in n2_3_5:
        if segments[1][0] in num and segments[1][1] in num:
            segments[3] = num
            n2_3_5.remove(num)
            break

    for num in n2_3_5:
        for seg in num:
            if seg not in segments[6]:
                break
        else:
            segments[5] = num
            n2_3_5.remove(num)
            segments[2] = n2_3_5.pop()
            break

    return segments

@read_file('data.txt')
def solution(data: list, part: int):
    outputs = [display.split(" | ")[1].split(" ") for display in data]

    if part == 1:
        return sum(sum(1 for num in display if len(num) in (2, 3, 4, 7)) for display in outputs)

    displays = [display.split(" | ")[0].split(" ") for display in data]

    answer = 0

    for i in range(len(displays)):
        number = ""
        decoder = __get_segments(displays[i])

        for num in outputs[i]:
            for j in range(len(decoder)):
                if set(decoder[j]) == set(num):
                    number += str(j)

        answer += int(number)

    return answer



if __name__ == '__main__':
    start = time.perf_counter()
    print(solution(1))
    print(time.perf_counter() - start)

    start = time.perf_counter()
    print(solution(2))
    print(time.perf_counter() - start)
