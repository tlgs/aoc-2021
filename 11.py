"""Day 11: Dumbo Octopus"""
import itertools
import sys


def adjacent(x, y):
    yield x - 1, y - 1
    yield x, y - 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x + 1, y
    yield x - 1, y + 1
    yield x, y + 1
    yield x + 1, y + 1


def parse_lines(stream):
    octopuses = {}
    for y, row in enumerate(stream):
        for x, v in enumerate(row.rstrip()):
            octopuses[(x, y)] = int(v)

    return octopuses


def flash(octopuses, coord):
    octopuses[coord] = 0
    counts = 0
    for t in adjacent(*coord):
        if t in octopuses and octopuses[t] != 0:
            if octopuses[t] + 1 > 9:
                counts += flash(octopuses, t)
            else:
                octopuses[t] += 1

    return 1 + counts


def simulate(octopuses, steps):
    total = 0
    for _ in range(steps):
        for k in octopuses:
            octopuses[k] += 1

        for k in octopuses:
            if octopuses[k] > 9:
                total += flash(octopuses, k)

    return total


def synchronous_flash(octopuses):
    n = len(octopuses)
    for i in itertools.count(start=1):
        for k in octopuses:
            octopuses[k] += 1

        total = 0
        for k in octopuses:
            if octopuses[k] > 9:
                total += flash(octopuses, k)

        if total == n:
            return i

    raise RuntimeError


class Test:
    example = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""".splitlines()

    def test_one(self):
        assert simulate(parse_lines(self.example), 100) == 1656

    def test_two(self):
        assert synchronous_flash(parse_lines(self.example)) == 195


def main():
    puzzle = parse_lines(sys.stdin)

    print("part 1:", simulate(puzzle.copy(), 100))
    print("part 2:", synchronous_flash(puzzle.copy()))


if __name__ == "__main__":
    main()
