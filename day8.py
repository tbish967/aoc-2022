from aoc import get_input
from enum import Enum

data = get_input(8).splitlines()


def coordAdd(a, b):
    return [a[0] + b[0], a[1] + b[1]]


class Direction(Enum):
    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Tree:
    def __init__(self, height):
        self.height = height
        self.maxNeighbors = {}


class Forest:
    def __init__(self, rows):
        self.trees = []
        for row in rows:
            self.trees.append([int(t) for t in row.split()])

    def getTallest(self, coord, direction):
        if (coord[0] < 0 or coord[0] > len(self.trees[0]) or
                coord[1] < 0 or coord[1] > len(self.trees[1])):
            return 0
        if direction in self.trees[coord[0]][coord[1]]:
            return

    def countHidden(self):
        for d in Direction:
            sadf


def part1():
    f = Forest(data)
    return f.countHidden()


def part2():
    return None


def main():
    part1_res = part1()
    print(f'Part 1: {part1_res}')

    part2_res = part2()
    print(f'Part 2: {part2_res}')


main()
