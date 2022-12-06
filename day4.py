from aoc import get_input

data = get_input(4).splitlines()
def parse(line):
    return [list(map(int, k.split('-'))) for k in line.split(',')]

def contains(x, y):
    return (x[0] <= y[0]) and (x[1] >= y[1])


def overlaps(x, y):
    return x[0] <= y[1] and x[1] >= y[0]

def part1():
    score = 0
    for line in data:
        r1, r2 = parse(line)
        if contains(r1, r2) or contains(r2, r1):
            score += 1
    return score

def part2():
    score = 0
    for line in data:
        r1, r2 = parse(line)
        if overlaps(r1, r2):
            score += 1
    return score


def main():
    part1_res = part1()
    print(f'Part 1: {part1_res}')

    part2_res = part2()
    print(f'Part 2: {part2_res}')

main()