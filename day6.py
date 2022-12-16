from aoc import get_input
from collections import deque

data = get_input(6)




def part1():
    window = deque()
    for i in range(len(data)):
        window.append(data[i])
        if len(window) >= 4:
            print(window)
            if len(window) == len(set(window)):
                return i+1
            window.popleft()

    return None


def part2():
    window = deque()
    for i in range(len(data)):
        window.append(data[i])
        if len(window) >= 14:
            print(window)
            if len(window) == len(set(window)):
                return i+1
            window.popleft()
    return None

def main():
    part1_res = part1()
    print(f'Part 1: {part1_res}')

    part2_res = part2()
    print(f'Part 2: {part2_res}')


main()
