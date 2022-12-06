from aoc import get_input
from collections import deque
import re

def parseStacks(input):
    ln = 0
    while input[ln][1] != '1':
        ln += 1
    nstacks = int(input[ln].split()[-1])

    ln = 0
    stacks = [deque() for i in range(nstacks)]
    while input[ln][1] != '1':
        line = input[ln]
        for i in range(0, len(line), 4):
            cval = line[i + 1]
            if cval.isalpha():
                stacks[i // 4].appendleft(cval)
        ln += 1
    return stacks

def parseMoves(input):
    ln = 0
    while input[ln][0:4] != 'move':
        ln += 1

    moves = []
    for line in input[ln:]:
        moves.append([int(k) for k in re.findall(r'move (\d+) from (\d+) to (\d+)', line)[0]])
    return moves

def doMove(stacks, move):
    for i in range(move[0]):
        stacks[move[2]-1].append(stacks[move[1]-1].pop())

def doOrderedMove(stacks, move):
    tmp = deque()
    for i in range(move[0]):
        tmp.appendleft(stacks[move[1]-1].pop())
    stacks[move[2]-1] += tmp

data = get_input(5).splitlines()

def part1():
    stacks = parseStacks(data)
    for move in parseMoves(data):
        doMove(stacks, move)
    return ''.join([stack[-1] for stack in stacks])

def part2():
    stacks = parseStacks(data)
    for move in parseMoves(data):
        print(stacks)
        print(move)
        doOrderedMove(stacks, move)
        print(stacks)
    return ''.join([stack[-1] for stack in stacks])
def main():
    part1_res = part1()
    print(f'Part 1: {part1_res}')

    part2_res = part2()
    print(f'Part 2: {part2_res}')
main()