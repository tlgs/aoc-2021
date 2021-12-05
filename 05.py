"""Day 5: Hydrothermal Venture"""
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
    once, twice = set(), set()
    for start, end in lines:
        x1, y1, x2, y2 = *start, *end

        if x2 == x1:
            sy = sig(y2 - y1)
            points = {(x1, i) for i in range(y1, y2 + sy, sy)}

        elif y2 == y1:
            sx = sig(x2 - x1)
            points = {(i, y1) for i in range(x1, x2 + sx, sx)}

        else:
            continue

        twice |= points & once
        once |= points

    return len(twice)


def overlap_two(lines):
    once, twice = set(), set()
    for start, end in lines:
        x1, y1, x2, y2 = *start, *end

        if x2 == x1:
            sy = sig(y2 - y1)
            points = {(x1, i) for i in range(y1, y2 + sy, sy)}

        elif y2 == y1:
            sx = sig(x2 - x1)
            points = {(i, y1) for i in range(x1, x2 + sx, sx)}

        elif abs((y2 - y1) / (x2 - x1)) == 1:
            sx = sig(x2 - x1)
            sy = sig(y2 - y1)
            points = {
                (i, j) for i, j in zip(range(x1, x2 + sx, sx), range(y1, y2 + sy, sy))
            }

        else:
            continue

        twice |= points & once
        once |= points

    return len(twice)


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
