"""Day 21: Dirac Dice"""
import functools
import itertools
import sys


def parse_input(puzzle_input):
    raw_a, raw_b = puzzle_input.splitlines()
    *_, a = raw_a.split()
    *_, b = raw_b.split()

    return int(a), int(b)


def part_one(a, b):
    positions = [a, b]
    scores = [0, 0]
    die_count = 0
    deterministic_die = itertools.cycle(range(1, 101))
    while not any(v >= 1000 for v in scores):
        for i in range(2):
            roll = sum(next(deterministic_die) for _ in range(3))
            positions[i] = (positions[i] + roll - 1) % 10 + 1
            scores[i] += positions[i]
            die_count += 1
            if scores[i] >= 1000:
                break

    return 3 * die_count * min(scores)


@functools.cache
def play(pa, pb, sa, sb):
    if sb >= 21:
        return 0, 1

    wins_a, wins_b = 0, 0
    for roll, n in [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]:
        new_pa = (pa + roll) % 10 or 10
        wb, wa = play(pb, new_pa, sb, sa + new_pa)

        wins_a += wa * n
        wins_b += wb * n

    return wins_a, wins_b


def part_two(a, b):
    return max(play(a, b, 0, 0))


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
