from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int

    def __repr__(self):
        return f"x: {self.x}\ny: {self.y}"

print(Point(x=1, y=2))