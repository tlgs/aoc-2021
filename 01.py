"""Day 1: Sonar Sweep

Lessons:
    `itertools.pairwise` becomes available on Python 3.10
"""
import sys
from collections import deque
from itertools import islice, tee


def _pairwise(iterable):
    """From: https://github.com/more-itertools/more-itertools"""
    a, b = tee(iterable)
    next(b, None)
    yield from zip(a, b)


def _sliding_window(iterable, n):
    """From: https://github.com/more-itertools/more-itertools"""
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def increasing(depths):
    return sum(b > a for a, b in _pairwise(depths))


def increasing_window(depths):
    return sum(sum(b) > sum(a) for a, b in _pairwise(_sliding_window(depths, 3)))


class TestClass:
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
