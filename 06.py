"""Day 6: Lanternfish

Lessons:
    `Counter.total()` becomes available in Python 3.10.
"""
import collections
import sys


def simulate(ages, days):
    school = collections.Counter(ages)
    for _ in range(days):
        prev = school.get(0, 0)
        for i in range(8, -1, -1):
            curr = school.get(i, 0)
            school[i] = prev
            if i == 0:
                school[6] += curr

            prev = curr

    return sum(v for v in school.values())


class Test:
    example = [3, 4, 3, 1, 2]

    def test_one(self):
        assert simulate(self.example, 80) == 5934

    def test_two(self):
        assert simulate(self.example, 256) == 26984457539


def main():
    puzzle = [int(x) for x in sys.stdin.read().split(",")]

    print("part 1:", simulate(puzzle, 80))
    print("part 2:", simulate(puzzle, 256))


if __name__ == "__main__":
    main()
