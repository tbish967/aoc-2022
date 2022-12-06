import heapq

from aoc import get_input

data = get_input(1).split('\n\n')


def part1():
    best = 0
    for elf in data:
        best = max(best, sum([int(line) for line in elf.splitlines()]))

    return best


def part2():
    tops = []
    for elf in data:
        cals = sum([int(line) for line in elf.splitlines()])
        if len(tops) < 3:
            heapq.heappush(tops, cals)
        else:
            heapq.heappushpop(tops, cals)

    return sum(tops)


def main():
    part1_res = part1()
    print(f'Part 1: {part1_res}')

    part2_res = part2()
    print(f'Part 2: {part2_res}')


main()
