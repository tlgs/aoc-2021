"""Day 23: Amphipod"""
import collections
import heapq
import itertools
import sys


def parse_input(puzzle_input):
    start = [[], [], [], []]
    d = {c: i for i, c in enumerate("ABCD")}
    for y, row in enumerate(puzzle_input.splitlines()):
        for x, v in enumerate(row):
            if (i := d.get(v)) is not None:
                start[i].append((x - 1, y - 1))

    return tuple(frozenset(a) for a in start)


def manhattan(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def part_one(start):
    hallway = set(itertools.product([0, 1, 3, 5, 7, 9, 10], [0]))
    rooms = set(itertools.product([2, 4, 6, 8], [1, 2]))

    neighbors = collections.defaultdict(list)
    distances = {}
    blocking = {}
    for p in hallway:
        for q in rooms:
            neighbors[p].append(q)
            neighbors[q].append(p)

            v = manhattan(p, q)
            distances[(p, q)] = v
            distances[(q, p)] = v

            xa, _ = p
            xb, yb = q
            blockers = set((x, _) for x, _ in hallway if xa > x > xb or xa < x < xb)
            if yb == 2:
                blockers.add((xb, 1))
            blocking[(p, q)] = blockers
            blocking[(q, p)] = blockers

    target = (
        frozenset([(2, 1), (2, 2)]),
        frozenset([(4, 1), (4, 2)]),
        frozenset([(6, 1), (6, 2)]),
        frozenset([(8, 1), (8, 2)]),
    )

    costs = {start: 0}
    queue = [(0, start)]
    while queue:
        cost, node = heapq.heappop(queue)
        if node == target:
            return cost

        # print(cost, node)
        occupied = set(t for fs in node for t in fs)
        for i, fs in enumerate(node):
            for t in fs:
                if t in hallway:
                    to_check = target[i]
                else:
                    to_check = neighbors[t]
                for p in to_check:
                    if p in occupied or any(x in occupied for x in blocking[t, p]):
                        continue

                    new_node = tuple(
                        amphi if i != j else frozenset(fs - {t} | {p})
                        for j, amphi in enumerate(node)
                    )
                    new_cost = cost + distances[t, p] * 10 ** i
                    if new_node not in costs or new_cost < costs[new_node]:
                        costs[new_node] = new_cost
                        heapq.heappush(queue, (new_cost, new_node))

    raise RuntimeError("unreachable")


def part_two(old_start):
    ...


class Test:
    example = """\
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
"""

    def test_one(self):
        assert part_one(parse_input(self.example)) == 12521

    def test_two(self):
        assert part_two(parse_input(self.example)) == 44169


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(puzzle))
    print("part 2:", part_two(puzzle))


if __name__ == "__main__":
    main()
