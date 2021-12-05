"""Day 5: Hydrothermal Venture"""
import collections
import itertools
import sys


def parse_lines(stream):
    output = []
    for raw_coords in (line.split(" -> ") for line in stream):
        split_coords = (raw_coord.split(",") for raw_coord in raw_coords)
        fst, snd = (tuple(int(a) for a in t) for t in split_coords)
        output.append((fst, snd))

    return output


def cmp(x):
    return (x > 0) - (x < 0)


def overlap_one(segments):
    counts = collections.defaultdict(int)
    for start, end in segments:
        x1, y1, x2, y2 = *start, *end

        if x1 == x2:
            dy = cmp(y2 - y1)
            for i in range(y1, y2 + dy, dy):
                counts[(x1, i)] += 1

        if y1 == y2:
            dx = cmp(x2 - x1)
            for i in range(x1, x2 + dx, dx):
                counts[(i, y1)] += 1

    return sum(v >= 2 for v in counts.values())


def overlap_two(segments):
    counts = collections.defaultdict(int)
    for start, end in segments:
        x1, y1, x2, y2 = *start, *end

        dx = cmp(x2 - x1)
        dy = cmp(y2 - y1)

        for i, j in zip(
            range(x1, x2 + dx, dx) if dx else itertools.repeat(x1),
            range(y1, y2 + dy, dy) if dy else itertools.repeat(y1),
        ):
            counts[(i, j)] += 1

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
