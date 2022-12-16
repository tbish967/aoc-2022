from aoc import get_input
from dataclasses import dataclass

data = get_input(7).splitlines()

@dataclass
class File:
    size: int
    name: str

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = {}
        self.size = 0
        self.files = []

    def getChildrenUnder(self, max):
        s = 0
        for child in self.children.values():
            s += child.getChildrenUnder(max)
        if self.size <= max:
            s += self.size
        return s

    def freeSpace(self, toFree):
        cmins = [c.freeSpace(toFree) for c in self.children.values()]
        if self.size >= toFree:
            print(self.name, self.size)
            cmins.append(self.size)
        if len(cmins) > 0:
            return min(cmins)
        return float('inf')

    def addSize(self, size):
        self.size += size
        if self.parent:
            self.parent.addSize(size)

    def addFile(self, file: File):
        self.files.append(file)
        self.addSize(file.size)

    def addChild(self, name):
        self.children[name] = Directory(name, parent=self)
def parseInput(input) -> Directory:
    i = 0
    head = Directory('HEAD')
    head.addChild('/')
    cur = head
    while i < len(input):
        line = input[i].split()
        if line[0] != '$':
            raise Exception('Unexpected output line')

        if line[1] == 'cd':
            if line[2] == '..':
                cur = cur.parent
            else:
                cur = cur.children[line[2]]
        elif line[1] == 'ls':
            i += 1
            while i < len(input) and input[i][0] != '$':
                line = input[i].split()
                if line[0] == 'dir':
                    cur.addChild(line[1])
                else:
                    cur.addFile(File(int(line[0]), line[1]))
                i += 1
            i -= 1
        i += 1
    return head.children['/']

def part1():
    root = parseInput(data)
    return root.getChildrenUnder(100000)

def part2():
    root = parseInput(data)
    print(root.size)
    return root.freeSpace(root.size - 40000000)
def main():
    part1_res = part1()
    print(f'Part 1: {part1_res}')

    part2_res = part2()
    print(f'Part 2: {part2_res}')
main()