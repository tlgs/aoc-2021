"""Day 15: Chiton

Algorithm:
    Dijkstra, with no need to revisit previously seen nodes

Lessons:
    Remember to use `maxsize=None` when using `lru_cache`- by default it will
    only store the latest 128 calls. Using `lru_cache` without this argument
    actually resulted in a decrease in performance.

    More importantly, don't scorn on raw lists / lists of lists as they might
    outperform queues / dicts when _memory doesn't matter_ and you can solve the problem
    with appends and lookups (both O(1)).
"""
import sys


def parse_input(puzzle_input):
    grid = []
    for row in puzzle_input.splitlines():
        grid.append([int(x) for x in row])

    return grid


def neighbors(x, y):
    yield x, y - 1
    yield x - 1, y
    yield x + 1, y
    yield x, y + 1


def part_one(grid):
    side = len(grid)
    end = side - 1

    dist = [[0] * side for _ in range(side)]
    queue = [[(0, 0)]] + [[] for _ in range(side * 18)]
    v = 0
    while not dist[end][end]:
        for x, y in queue[v]:
            for p, q in neighbors(x, y):
                if p < 0 or p > end or q < 0 or q > end:
                    continue

                if not dist[q][p]:
                    w = grid[q][p]
                    dist[q][p] = v + w
                    queue[v + w].append((p, q))

        v += 1

    return dist[end][end]


def part_two(grid):
    side = len(grid)
    end = side * 5 - 1

    dist = [[0] * side * 5 for _ in range(side * 5)]
    queue = [[(0, 0)]] + [[] for _ in range(side * 90)]
    v = 0
    while not dist[end][end]:
        for x, y in queue[v]:
            for p, q in neighbors(x, y):
                if p < 0 or p > end or q < 0 or q > end:
                    continue

                if not dist[q][p]:
                    w = ((grid[q % side][p % side] + p // side + q // side - 1) % 9) + 1
                    dist[q][p] = v + w
                    queue[v + w].append((p, q))

        v += 1

    return dist[end][end]


class Test:
    example = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""

    def test_one(self):
        assert part_one(parse_input(self.example)) == 40

    def test_two(self):
        assert part_two(parse_input(self.example)) == 315


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(puzzle))
    print("part 2:", part_two(puzzle))


if __name__ == "__main__":
    main()
