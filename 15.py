"""Day 15: Chiton

Algorithm:
    Dijkstra

Lessons:
    Remember to use `maxsize=None` when using `lru_cache`- by default it will
    only store the latest 128 calls. Using `lru_cache` without this argument
    actually resulted in a decrease in performance.

    More importantly, don't scorn on raw lists / lists of lists as they might
    outperform queues / dicts when _memory doesn't matter_ and you can solve the problem
    with appends and lookups (both O(1)).
"""
import sys
from heapq import heappop, heappush


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
    end = len(grid) - 1
    total_costs = {(0, 0): 0}

    frontier = []
    heappush(frontier, (0, (0, 0)))
    while frontier:
        curr_cost, curr = heappop(frontier)
        if curr == (end, end):
            break

        for x, y in neighbors(*curr):
            if x < 0 or x > end or y < 0 or y > end:
                continue

            new_cost = curr_cost + grid[y][x]
            if (x, y) not in total_costs:
                total_costs[x, y] = new_cost
                heappush(frontier, (new_cost, (x, y)))

    return total_costs[end, end]


def part_two(grid):
    side = len(grid)
    end = side * 5 - 1

    dist = [[0] * side * 5 for _ in range(side * 5)]
    queue = [[(0, 0)]] + [[] for _ in range(side * 90)]
    v = 0
    while dist[end][end] == 0:
        for y, x in queue[v]:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if x + dx < 0 or x + dx > end or y + dy < 0 or y + dy > end:
                    continue

                if dist[y + dy][x + dx] == 0:
                    dt = (
                        (
                            grid[(y + dy) % side][(x + dx) % side]
                            + (x + dx) // side
                            + (y + dy) // side
                            - 1
                        )
                        % 9
                    ) + 1

                    dist[y + dy][x + dx] = v + dt
                    queue[v + dt].append((y + dy, x + dx))

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
