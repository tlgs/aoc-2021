"""Day 12: Passage Pathing"""
import collections
import functools
import sys

import pytest


def parse_lines(stream):
    edges = collections.defaultdict(list)
    for line in stream:
        a, b = line.rstrip().split("-")
        edges[a].append(b)
        edges[b].append(a)

    for k in edges:
        edges[k] = tuple(edges[k])

    # frozendict when
    FrozenEdges = collections.namedtuple("FrozenEdges", edges.keys())
    fe = FrozenEdges(**edges)
    return fe


@functools.lru_cache(maxsize=None)
def dfs(edges, curr, seen, twice=True):
    counts = 0
    for node in getattr(edges, curr):
        if node == "end":
            counts += 1

        elif not node.islower():
            counts += dfs(edges, node, seen, twice)

        elif node != "start":
            if node not in seen:
                counts += dfs(edges, node, seen | {node}, twice)
            elif not twice:
                counts += dfs(edges, node, seen | {node}, True)

    return counts


def distinct_paths_one(edges):
    return dfs(edges, "start", frozenset())


def distinct_paths_two(edges):
    return dfs(edges, "start", frozenset(), False)


EXAMPLE1 = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
""".splitlines()

EXAMPLE2 = """\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
""".splitlines()

EXAMPLE3 = """\
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
""".splitlines()


class Test:
    @pytest.mark.parametrize(
        "test_input,expected",
        [(EXAMPLE1, 10), (EXAMPLE2, 19), (EXAMPLE3, 226)],
    )
    def test_one(self, test_input, expected):
        assert distinct_paths_one(parse_lines(test_input)) == expected

    @pytest.mark.parametrize(
        "test_input,expected",
        [(EXAMPLE1, 36), (EXAMPLE2, 103), (EXAMPLE3, 3509)],
    )
    def test_two(self, test_input, expected):
        assert distinct_paths_two(parse_lines(test_input)) == expected


def main():
    puzzle = parse_lines(sys.stdin)

    print("part 1:", distinct_paths_one(puzzle))
    print("part 2:", distinct_paths_two(puzzle))


if __name__ == "__main__":
    main()
