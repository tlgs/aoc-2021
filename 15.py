"""Day 15: Chiton"""
import sys
from heapq import heappop, heappush


def parse_input(puzzle_input):
    grid = {}
    for y, row in enumerate(puzzle_input.splitlines()):
        for x, v in enumerate(row):
            grid[x, y] = int(v)

    return grid


def neighbors(x, y):
    yield x, y - 1
    yield x - 1, y
    yield x + 1, y
    yield x, y + 1


def a_star(grid, full=False):
    x_max = max(k[0] for k in grid.keys())
    y_max = max(k[1] for k in grid.keys())

    if full:
        end = ((x_max + 1) * 5) - 1, ((y_max + 1) * 5) - 1
    else:
        end = x_max, y_max

    backtrack = {(0, 0): None}
    total_costs = {(0, 0): 0}

    frontier = []
    heappush(frontier, (0, (0, 0)))
    while frontier:
        _, (x, y) = heappop(frontier)
        if (x, y) == end:
            break

        for p, q in neighbors(x, y):
            if p < 0 or q < 0 or p > end[0] or q > end[1]:
                continue

            p_div, p_mod = divmod(p, x_max + 1)
            q_div, q_mod = divmod(q, y_max + 1)
            raw_step_cost = grid[p_mod, q_mod] + p_div + q_div  # max should be 17
            step_cost = sum(divmod(raw_step_cost, 10))
            new_cost = total_costs[x, y] + step_cost
            if (p, q) not in total_costs or new_cost < total_costs[p, q]:
                total_costs[p, q] = new_cost
                backtrack[p, q] = x, y

                manhattan = (end[0] - p) + (end[1] - q)
                heappush(frontier, (new_cost + manhattan, (p, q)))

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
        assert a_star(parse_input(self.example)) == 40

    def test_two(self):
        assert a_star(parse_input(self.example), True) == 315


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", a_star(puzzle))
    print("part 2:", a_star(puzzle, True))


if __name__ == "__main__":
    main()
