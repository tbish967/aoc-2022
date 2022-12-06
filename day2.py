from aoc import get_input


class Shape:
    def __init__(self, score, loses=None, beats=None):
        self.score = score
        self.loses = loses
        self.beats = beats


class Hand:
    hmap = {
        'A': ('rock', 1),
        'B': ('paper', 2),
        'C': ('scissors', 3),
        'X': ('rock', 1),
        'Y': ('paper', 2),
        'Z': ('scissors', 3)
    }

    def __init__(self, letter):
        self.hnd = self.hmap[letter][0]
        self.score = self.hmap[letter][1]

    def __lt__(self, other):
        if ((self.hnd == 'rock' and other.hnd == 'paper') or
                (self.hnd == 'paper' and other.hnd == 'scissors') or
                (self.hnd == 'scissors' and other.hnd == 'rock')):
            return True
        return False

    def __eq__(self, other):
        if self.hnd == other.hnd:
            return True
        return False


def part1():
    score = 0
    for line in get_input(2).splitlines():
        throws = line.split()
        opp, me = Hand(throws[0]), Hand(throws[1])

        score += me.score
        if me > opp:
            score += 6
        elif me == opp:
            score += 3

    return score


def part2():
    rock = Shape(1)
    paper = Shape(2)
    scissors = Shape(3)
    rock.loses, rock.beats = paper, scissors
    paper.loses, paper.beats = scissors, rock
    scissors.loses, scissors.beats = rock, paper
    smap = {
        'A': rock,
        'B': paper,
        'C': scissors,
    }

    score = 0
    for line in get_input(2).splitlines():
        throws = line.split()
        opp, res = smap[throws[0]], throws[1]

        if res == 'X':
            score += opp.beats.score
        elif res == 'Y':
            score += 3 + opp.score
        elif res == 'Z':
            score += 6 + opp.loses.score

    return score


def main():
    part1_res = part1()
    print(f'Part 1: {part1_res}')

    part2_res = part2()
    print(f'Part 2: {part2_res}')


main()
