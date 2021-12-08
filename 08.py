"""Day 8: Seven Segment Search"""
import collections
import functools
import sys


def easy_digits(puzzle):
    counts = 0
    for _, output in puzzle:
        counts += sum(len(seq) in {2, 3, 4, 7} for seq in output)

    return counts


def outputs_sum(puzzle):
    total = 0
    for patterns, outputs in puzzle:
        segments = collections.defaultdict(list)
        for p in patterns:
            segments[len(p)].append(set(p))

        cf = segments[2][0]
        bd = segments[4][0] - segments[2][0]
        abfg = functools.reduce(set.intersection, segments[6])

        a = segments[3][0] - segments[2][0]

        f = cf & abfg
        b = bd & abfg

        c = segments[2][0] - f
        d = segments[4][0] - (b | c | f)

        g = abfg - (a | b | f)

        e = segments[7][0] - (a | b | c | d | f | g)

        translator = {
            frozenset(a | b | c | e | f | g): "0",
            frozenset(c | f): "1",
            frozenset(a | c | d | e | g): "2",
            frozenset(a | c | d | f | g): "3",
            frozenset(b | c | d | f): "4",
            frozenset(a | b | d | f | g): "5",
            frozenset(a | b | d | e | f | g): "6",
            frozenset(a | c | f): "7",
            frozenset(a | b | c | d | e | f | g): "8",
            frozenset(a | b | c | d | f | g): "9",
        }
        n = "".join([translator[frozenset(x)] for x in outputs])
        total += int(n)

    return total


class Test:
    example = [
        (
            [
                "be",
                "cfbegad",
                "cbdgef",
                "fgaecd",
                "cgeb",
                "fdcge",
                "agebfd",
                "fecdb",
                "fabcd",
                "edb",
            ],
            ["fdgacbe", "cefdb", "cefbgd", "gcbe"],
        ),
        (
            [
                "edbfga",
                "begcd",
                "cbg",
                "gc",
                "gcadebf",
                "fbgde",
                "acbgfd",
                "abcde",
                "gfcbed",
                "gfec",
            ],
            ["fcgedb", "cgb", "dgebacf", "gc"],
        ),
        (
            [
                "fgaebd",
                "cg",
                "bdaec",
                "gdafb",
                "agbcfd",
                "gdcbef",
                "bgcad",
                "gfac",
                "gcb",
                "cdgabef",
            ],
            ["cg", "cg", "fdcagb", "cbg"],
        ),
        (
            [
                "fbegcd",
                "cbd",
                "adcefb",
                "dageb",
                "afcb",
                "bc",
                "aefdc",
                "ecdab",
                "fgdeca",
                "fcdbega",
            ],
            ["efabcd", "cedba", "gadfec", "cb"],
        ),
        (
            [
                "aecbfdg",
                "fbg",
                "gf",
                "bafeg",
                "dbefa",
                "fcge",
                "gcbea",
                "fcaegb",
                "dgceab",
                "fcbdga",
            ],
            ["gecf", "egdcabf", "bgf", "bfgea"],
        ),
        (
            [
                "fgeab",
                "ca",
                "afcebg",
                "bdacfeg",
                "cfaedg",
                "gcfdb",
                "baec",
                "bfadeg",
                "bafgc",
                "acf",
            ],
            ["gebdcfa", "ecba", "ca", "fadegcb"],
        ),
        (
            [
                "dbcfg",
                "fgd",
                "bdegcaf",
                "fgec",
                "aegbdf",
                "ecdfab",
                "fbedc",
                "dacgb",
                "gdcebf",
                "gf",
            ],
            ["cefg", "dcbef", "fcge", "gbcadfe"],
        ),
        (
            [
                "bdfegc",
                "cbegaf",
                "gecbf",
                "dfcage",
                "bdacg",
                "ed",
                "bedf",
                "ced",
                "adcbefg",
                "gebcd",
            ],
            ["ed", "bcgafe", "cdgba", "cbgef"],
        ),
        (
            [
                "egadfb",
                "cdbfeg",
                "cegd",
                "fecab",
                "cgb",
                "gbdefca",
                "cg",
                "fgcdab",
                "egfdb",
                "bfceg",
            ],
            ["gbdfcae", "bgc", "cg", "cgb"],
        ),
        (
            [
                "gcafb",
                "gcf",
                "dcaebfg",
                "ecagb",
                "gf",
                "abcdeg",
                "gaef",
                "cafbge",
                "fdbac",
                "fegbdc",
            ],
            ["fgae", "cfgab", "fg", "bagce"],
        ),
    ]

    def test_one(self):
        assert easy_digits(self.example) == 26

    def test_two(self):
        assert outputs_sum(self.example) == 61229


def main():
    puzzle = []
    for line in sys.stdin:
        patterns, outputs = [x.split() for x in line.split("|")]
        puzzle.append((patterns, outputs))

    print("part 1:", easy_digits(puzzle))
    print("part 2:", outputs_sum(puzzle))


if __name__ == "__main__":
    main()
