"""Day 5: Hydrothermal Venture"""
import collections
import sys


def parse_lines(stream):
    output = []
    for raw_coords in (line.split(" -> ") for line in stream):
        split_coords = (raw_coord.split(",") for raw_coord in raw_coords)
        fst, snd = (tuple(int(a) for a in t) for t in split_coords)
        output.append((fst, snd))

    return output


def sig(x):
    return (-1) ** (x < 0)


def overlap_one(lines):
    counts = collections.defaultdict(int)
    for start, end in lines:
        x1, y1, x2, y2 = *start, *end
        dx, dy = (x2 - x1), (y2 - y1)

        if dx == 0:
            s = sig(dy)
            points = ((x1, i) for i in range(y1, y2 + s, s))
            for point in points:
                counts[point] += 1

        elif dy == 0:
            s = sig(dx)
            points = ((i, y1) for i in range(x1, x2 + s, s))
            for point in points:
                counts[point] += 1

    return sum(v >= 2 for v in counts.values())


def overlap_two(lines):
    counts = collections.defaultdict(int)
    for start, end in lines:
        x1, y1, x2, y2 = *start, *end
        dx, dy = (x2 - x1), (y2 - y1)
        sx, sy = sig(dx), sig(dy)

        if dx == 0:
            points = ((x1, i) for i in range(y1, y2 + sy, sy))
            for point in points:
                counts[point] += 1

        elif dy == 0:
            points = ((i, y1) for i in range(x1, x2 + sx, sx))
            for point in points:
                counts[point] += 1

        elif abs(dy / dx) == 1:
            points = (
                (i, j) for i, j in zip(range(x1, x2 + sx, sx), range(y1, y2 + sy, sy))
            )
            for point in points:
                counts[point] += 1

    return sum(v >= 2 for v in counts.values())


class Test:
    example = [
        ((0, 9), (5, 9)),
        ((8, 0), (0, 8)),
        ((9, 4), (3, 4)),
        ((2, 2), (2, 1)),
        ((7, 0), (7, 4)),
        ((6, 4), (2, 0)),
        ((0, 9), (2, 9)),
        ((3, 4), (1, 4)),
        ((0, 0), (8, 8)),
        ((5, 5), (8, 2)),
    ]

    def test_one(self):
        assert overlap_one(self.example) == 5

    def test_two(self):
        assert overlap_two(self.example) == 12


def main():
    puzzle = parse_lines(sys.stdin)

    print("part 1:", overlap_one(puzzle))
    print("part 2:", overlap_two(puzzle))


if __name__ == "__main__":
    main()
