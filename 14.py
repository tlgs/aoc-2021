"""Day 14: Extended Polymerization"""
import collections
import itertools
import sys


def parse_input(puzzle_input):
    template, raw_rules = puzzle_input.split("\n\n")

    rules = {}
    for line in raw_rules.splitlines():
        a, e = line.split(" -> ")
        rules[a] = (a[0] + e, e + a[1])

    return template, rules


def process_polymer(template, rules, steps):
    pairs = collections.Counter()
    ita, itb = itertools.tee(template)
    start = next(itb)
    for a, b in zip(ita, itb):
        pairs[a + b] += 1

    for _ in range(steps):
        nxt = collections.Counter()
        for k, v in pairs.items():
            for new_pairs in rules[k]:
                nxt[new_pairs] += v

        pairs = nxt

    counts = collections.Counter()
    for k, v in pairs.items():
        counts[k[1]] += v

    counts[start] += 1

    first, *_, last = counts.most_common()
    return first[1] - last[1]


class Test:
    example = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

    def test_one(self):
        assert process_polymer(*parse_input(self.example), 10) == 1588

    def test_two(self):
        assert process_polymer(*parse_input(self.example), 40) == 2188189693529


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", process_polymer(*puzzle, 10))
    print("part 2:", process_polymer(*puzzle, 40))


if __name__ == "__main__":
    main()
