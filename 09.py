"""Day 9: Smoke Basin"""
import sys


def risk_low_points(heightmap):
    n = len(heightmap)
    m = len(heightmap[0]) if n else 0

    def surrounding(x, y):
        yield heightmap[y - 1][x] if y > 0 else None
        yield heightmap[y][x - 1] if x > 0 else None
        yield heightmap[y][x + 1] if x < (m - 1) else None
        yield heightmap[y + 1][x] if y < (n - 1) else None

    total = 0
    for y, row in enumerate(heightmap):
        for x, v in enumerate(row):
            if all(v < w for w in surrounding(x, y) if w is not None):
                total += v + 1

    return total


def mult_three_largest_basins(heightmap):
    n = len(heightmap)
    m = len(heightmap[0]) if n else 0

    def surrounding(x, y):
        yield (x, y - 1) if y > 0 else None
        yield (x - 1, y) if x > 0 else None
        yield (x + 1, y) if x < (m - 1) else None
        yield (x, y + 1) if y < (n - 1) else None

    low_points = []
    for y, row in enumerate(heightmap):
        for x, v in enumerate(row):
            if all(
                v < heightmap[t[1]][t[0]] for t in surrounding(x, y) if t is not None
            ):
                low_points.append((x, y))

    basin_sizes = []
    for start in low_points:
        count = 0
        seen = set()
        stack = [start]
        while stack:
            x, y = stack.pop()
            count += 1
            for i, j in (
                t for t in surrounding(x, y) if t is not None and t not in seen
            ):
                v = heightmap[j][i]
                if v < 9 and v > heightmap[y][x]:
                    seen.add((i, j))
                    stack.append((i, j))

        basin_sizes.append(count)

    a, b, c, *_ = sorted(basin_sizes, reverse=True)
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
