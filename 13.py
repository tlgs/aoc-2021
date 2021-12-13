"""Day 13: Transparent Origami"""
import sys


def parse_lines(input_string):
    dots_list, fold_instructions = input_string.split("\n\n")

    dots = set()
    for entry in dots_list.splitlines():
        x, y = map(int, entry.split(","))
        dots.add((x, y))

    folds = []
    for entry in fold_instructions.splitlines():
        *_, fold_line = entry.split()
        axis, v = fold_line.split("=")
        folds.append((axis, int(v)))

    return dots, folds


def do_one_fold(dots, folds):
    axis, v = folds[0]
    paper = set()
    if axis == "y":
        for x, y in dots:
            if y < v:
                paper.add((x, y))
            else:
                paper.add((x, v - (y - v)))
    else:
        for x, y in dots:
            if x < v:
                paper.add((x, y))
            else:
                paper.add((v - (x - v), y))

    return len(paper)


def complete_folds(dots, folds):
    curr = dots.copy()
    y_max, x_max = sys.maxsize, sys.maxsize
    for axis, v in folds:
        prev = curr
        curr = set()
        if axis == "y":
            y_max = v
            for x, y in prev:
                if y < v:
                    curr.add((x, y))
                else:
                    curr.add((x, v - (y - v)))
        else:
            x_max = v
            for x, y in prev:
                if x < v:
                    curr.add((x, y))
                else:
                    curr.add((v - (x - v), y))

    out = [""]
    for y in range(y_max):
        row = []
        for x in range(x_max):
            row.append("#" if (x, y) in curr else ".")
        out.append("".join(row))

    return "\n".join(out)


class Test:
    example = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

    def test_one(self):
        assert do_one_fold(*parse_lines(self.example)) == 17


def main():
    puzzle = parse_lines(sys.stdin.read())

    print("part 1:", do_one_fold(*puzzle))
    print("part 2:", complete_folds(*puzzle))


if __name__ == "__main__":
    main()
