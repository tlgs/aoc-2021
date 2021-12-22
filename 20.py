"""Day 20: Trench Map"""
import sys


def parse_input(puzzle_input):
    algorithm, rest = puzzle_input.split("\n\n")
    lines = rest.splitlines()

    lit = set()
    for y, row in enumerate(lines):
        for x, value in enumerate(row):
            if value == "#":
                lit.add((x, y))

    bounds = len(lines[0]), len(lines)
    return algorithm, lit, bounds


def square(x, y):
    yield x - 1, y - 1
    yield x, y - 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x, y
    yield x + 1, y
    yield x - 1, y + 1
    yield x, y + 1
    yield x + 1, y + 1


def part_one(algorithm, lit, bounds):
    blink = algorithm[0] == "#" and algorithm[511] == "."
    x_max, y_max = bounds
    x_min, y_min = 0, 0

    image = lit.copy()
    for i in range(2):
        next_image = set()
        for y in range(y_min - 2, y_max + 3):
            for x in range(x_min - 2, x_max + 3):
                idx = 0
                for j, (p, q) in enumerate(square(x, y)):
                    if x_min <= p <= x_max and y_min <= q <= y_max:
                        light = (p, q) in image
                    else:
                        light = blink and i % 2 != 0
                    idx += light * 2 ** (8 - j)

                if algorithm[idx] == "#":
                    next_image.add((x, y))

        x_max, y_max = x_max + 2, y_max + 2
        x_min, y_min = x_min - 2, y_min - 2
        image = next_image

    return sum(x_min <= x <= x_max and y_min <= y <= y_max for x, y in image)


def part_two(algorithm, lit, bounds):
    blink = algorithm[0] == "#" and algorithm[511] == "."
    x_max, y_max = bounds
    x_min, y_min = 0, 0

    image = lit.copy()
    for i in range(50):
        next_image = set()
        for y in range(y_min - 2, y_max + 3):
            for x in range(x_min - 2, x_max + 3):
                idx = 0
                for j, (p, q) in enumerate(square(x, y)):
                    if x_min <= p <= x_max and y_min <= q <= y_max:
                        light = (p, q) in image
                    else:
                        light = blink and i % 2 != 0
                    idx += light * 2 ** (8 - j)

                if algorithm[idx] == "#":
                    next_image.add((x, y))

        x_max, y_max = x_max + 2, y_max + 2
        x_min, y_min = x_min - 2, y_min - 2
        image = next_image

    return sum(x_min <= x <= x_max and y_min <= y <= y_max for x, y in image)


class Test:
    example = """\
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 35

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 3351


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    main()
