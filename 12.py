"""Day 12: Passage Pathing"""
import collections
import sys

import pytest


def parse_lines(stream):
    edges = collections.defaultdict(list)
    for line in stream:
        a, b = line.rstrip().split("-")

        edges[a].append(b)
        edges[b].append(a)

    return edges


def distinct_paths(edges):
    count = 0
    stack = [["start"]]
    while stack:
        path = stack.pop()
        seen = {v for v in path if v.islower()}
        for node in edges[path[-1]]:
            if node == "end":
                count += 1
                continue

            elif node in seen:
                continue

            else:
                stack.append(path + [node])

    return count


def distinct_paths_two(edges):
    count = 0
    stack = [(["start"], False)]
    while stack:
        path, twice = stack.pop()
        seen = {v for v in path if v.islower()}
        for node in edges[path[-1]]:
            if node == "start":
                continue

            elif node == "end":
                count += 1
                continue

            elif node in seen:
                if twice:
                    continue
                stack.append((path + [node], True))

            else:
                stack.append((path + [node], twice))

    return count


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
        assert distinct_paths(parse_lines(test_input)) == expected

    @pytest.mark.parametrize(
        "test_input,expected",
        [(EXAMPLE1, 36), (EXAMPLE2, 103), (EXAMPLE3, 3509)],
    )
    def test_two(self, test_input, expected):
        assert distinct_paths_two(parse_lines(test_input)) == expected


def main():
    puzzle = parse_lines(sys.stdin)

    print("part 1:", distinct_paths(puzzle))
    print("part 2:", distinct_paths_two(puzzle))


if __name__ == "__main__":
    main()
