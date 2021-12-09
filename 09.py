"""Day 9: Smoke Basin"""
import sys


def surrounding(x, y):
    yield x, y - 1
    yield x - 1, y
    yield x + 1, y
    yield x, y + 1


def risk_low_points(heightmap):
    total = 0
    for y, row in enumerate(heightmap):
        for x, v in enumerate(row):
            for p, q in surrounding(x, y):
                try:
                    if heightmap[q][p] < v:
                        break
                except IndexError:
                    continue
            else:
                total += v + 1

    return total


def mult_three_largest_basins(heightmap):
    upstream = {}
    low_points = []
    for y, row in enumerate(heightmap):
        for x, v in enumerate(row):
            bigger_neighbours = []
            low = True
            for p, q in surrounding(x, y):
                try:
                    if q < 0 or p < 0:
                        raise IndexError
                    w = heightmap[q][p]
                except IndexError:
                    continue

                if w < v:
                    low = False
                elif w > v and w != 9:
                    bigger_neighbours.append((p, q))

            if low:
                low_points.append((x, y))
            upstream[(x, y)] = bigger_neighbours

    basins = []
    seen = set()
    for start in low_points:
        count = 0
        stack = [start]
        while stack:
            x, y = stack.pop()
            count += 1
            for point in upstream[(x, y)]:
                if point not in seen:
                    seen.add(point)
                    stack.append(point)

        basins.append(count)

    a, b, c, *_ = sorted(basins, reverse=True)
    return a * b * c


class Test:
    example = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]

    def test_one(self):
        assert risk_low_points(self.example) == 15

    def test_two(self):
        assert mult_three_largest_basins(self.example) == 1134


def main():
    puzzle = []
    for line in sys.stdin:
        puzzle.append([int(c) for c in line.rstrip()])

    print("part 1:", risk_low_points(puzzle))
    print("part 2:", mult_three_largest_basins(puzzle))


if __name__ == "__main__":
    main()
