"""Day 21: Dirac Dice"""
import functools
import sys


def parse_input(puzzle_input):
    raw_a, raw_b = puzzle_input.splitlines()
    *_, a = raw_a.split()
    *_, b = raw_b.split()

    return int(a), int(b)


def part_one(a, b):
    def deterministic(pa, pb, sa=0, sb=0, i=0):
        if sb >= 1000:
            return i * sa

        new_pa = (pa + 3 * i + 6) % 10 or 10
        return deterministic(pb, new_pa, sb, sa + new_pa, i + 3)

    return deterministic(a, b)


def part_two(a, b):
    @functools.cache
    def dirac(pa, pb, sa=0, sb=0):
        if sb >= 21:
            return 0, 1

        wins_a, wins_b = 0, 0
        for roll, n in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
            new_pa = (pa + roll) % 10 or 10
            wb, wa = dirac(pb, new_pa, sb, sa + new_pa)
            wins_a += wa * n
            wins_b += wb * n

        return wins_a, wins_b

    return max(dirac(a, b))


class Test:
    example = """\
Player 1 starting position: 4
Player 2 starting position: 8
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 739785

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 444356092776315


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    main()
