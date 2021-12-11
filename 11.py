"""Day 11: Dumbo Octopus"""
import copy
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


def simulate(octopuses, steps):
    flashes = 0
    for _ in range(steps):
        for x, y in octopuses:
            octopuses[x, y] += 1
        while True:
            for (x, y), v in octopuses.items():
                if v > 9:
                    flashes += 1
                    octopuses[x, y] = 0
                    for t in adjacent(x, y):
                        if t in octopuses and octopuses[t] != 0:
                            octopuses[t] += 1
                    break
            else:
                break

    return flashes


def synchronous_flash(octopuses):
    for i in itertools.count(start=1):
        flashes = 0
        for x, y in octopuses:
            octopuses[x, y] += 1
        while True:
            for (x, y), v in octopuses.items():
                if v > 9:
                    octopuses[x, y] = 0
                    flashes += 1
                    for t in adjacent(x, y):
                        if t in octopuses and octopuses[t] != 0:
                            octopuses[t] += 1
                    break
            else:
                break

        if flashes == 100:
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

    print("part 1:", simulate(copy.deepcopy(puzzle), 100))
    print("part 2:", synchronous_flash(puzzle))


if __name__ == "__main__":
    main()
