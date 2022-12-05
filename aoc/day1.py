from aoc import get_input
import heapq

data = get_input(1).split('\n\n')

best = 0
for elf in data:
    best = max(best, sum([int(line) for line in elf.splitlines()]))

print(best)

tops = []
for elf in data:
    cals = sum([int(line) for line in elf.splitlines()])
    if len(tops) < 3:
        heapq.heappush(tops, cals)
    else:
        heapq.heappushpop(tops, cals)

print(sum(tops))