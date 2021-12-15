"""Day 15: Chiton

Algorithm:
    Dijkstra

Lessons:
    Remember to use `maxsize=None` when using `lru_cache`- by default it will
    only store the latest 128 calls. Using `lru_cache` without this argument
    actually resulted in a decrease in performance.
"""
import functools
import sys
from heapq import heappop, heappush


def parse_input(puzzle_input):
    grid = {}
    for y, row in enumerate(puzzle_input.splitlines()):
        for x, v in enumerate(row):
            grid[x, y] = int(v)

    return grid, (x, y)


def neighbors(x, y):
    yield x, y - 1
    yield x - 1, y
    yield x + 1, y
    yield x, y + 1


def part_one(grid, end):
    total_costs = {(0, 0): 0}

    frontier = []
    heappush(frontier, (0, (0, 0)))
    while frontier:
        curr_cost, curr = heappop(frontier)
        if curr == end:
            break

        for neighbor in neighbors(*curr):
            if neighbor not in grid:
                continue

            new_cost = curr_cost + grid[neighbor]
            if neighbor not in total_costs or new_cost < total_costs[neighbor]:
                total_costs[neighbor] = new_cost
                heappush(frontier, (new_cost, neighbor))

    return total_costs[end]


def part_two(grid, end):
    side = end[0] + 1

    @functools.lru_cache(maxsize=None)
    def full_grid(x, y):
        v = grid[x % side, y % side] + x // side + y // side
        return v if v < 10 else v - 9

    end = side * 5 - 1, side * 5 - 1
    total_costs = {(0, 0): 0}
    frontier = []
    heappush(frontier, (0, (0, 0)))
    while frontier:
        curr_cost, curr = heappop(frontier)
        if curr == end:
            break

        for neighbor in neighbors(*curr):
            if not (-1 < neighbor[0] < side * 5) or not (-1 < neighbor[1] < side * 5):
                continue

            new_cost = curr_cost + full_grid(*neighbor)
            if neighbor not in total_costs or new_cost < total_costs[neighbor]:
                total_costs[neighbor] = new_cost
                heappush(frontier, (new_cost, neighbor))

    return total_costs[end]


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
        assert part_one(*parse_input(self.example)) == 40

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 315


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    main()
