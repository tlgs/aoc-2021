"""Day 6: The Treachery of Whales

Algorithm:
    The derivative of |x| is sign(x).
    ∑ sign(yi - x) equals zero only when the number of positive numbers equals
  the number of negative numbers; this happens when x = median{y1, y2, ..., yN}.
    See <https://math.stackexchange.com/a/1024462> for a good description.

    Second part was just a naive brute-force approach by identifying that
  fuel(|y - x|) = T(|y - x|) = (|y - x| * (|y - x| + 1)) / 2.
    Here, T(n) is the nth _triangular number_.
    See <https://en.wikipedia.org/wiki/Triangular_number>.
"""
import statistics
import sys


def fuel_linear(crabs):
    m = round(statistics.median(crabs))
    return sum(abs(m - x) for x in crabs)


def fuel_triangular(crabs):
    fuel = sys.maxsize
    for x in range(min(crabs), max(crabs)):
        v = sum((abs(x - y) * (abs(x - y) + 1)) / 2 for y in crabs)
        fuel = min(fuel, v)

    return int(fuel)


class Test:
    example = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    def test_one(self):
        assert fuel_linear(self.example) == 37

    def test_two(self):
        assert fuel_triangular(self.example) == 168


def main():
    puzzle = [int(x) for x in sys.stdin.read().split(",")]

    print("part 1:", fuel_linear(puzzle))
    print("part 2:", fuel_triangular(puzzle))


if __name__ == "__main__":
    main()
