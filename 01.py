"""Day 1: Sonar Sweep

Lessons:
    `itertools.pairwise` becomes available on Python 3.10.

    Using `collections.deque` with the `maxlen` argument makes implementing
    sliding windows trivial.
"""
import sys
from collections import deque
from itertools import islice, tee


def increasing(depths):
    a, b = tee(depths)
    next(b, None)
    return sum(prev < curr for prev, curr in zip(a, b))


def increasing_window(depths):
    total = 0
    it = iter(depths)
    window = deque(islice(it, 3))
    for x in it:
        window.append(x)
        total += x > window.popleft()

    return total


class Test:
    example = [99, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    def test_one(self):
        assert increasing(self.example) == 7

    def test_two(self):
        assert increasing_window(self.example) == 5


def main():
    puzzle = [int(x) for x in sys.stdin]

    print("part 1:", increasing(puzzle))
    print("part 2:", increasing_window(puzzle))


if __name__ == "__main__":
    main()
