"""Day 6: Lanternfish"""
import collections
import sys


def simulate(ages, days):
    school = collections.Counter(ages)
    for _ in range(days):
        resets = school.get(0, 0)
        for i in range(8):
            school[i] = school.get(i + 1, 0)

        school[8] = resets
        school[6] += resets

    return school.total()


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
