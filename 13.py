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
    if axis == "y":
        paper = {(x, y) if y < v else (x, v - (y - v)) for x, y in dots}
    else:
        paper = {(x, y) if x < v else (v - (x - v), y) for x, y in dots}

    return len(paper)


def complete_folds(dots, folds):
    paper = dots.copy()
    for axis, v in folds:
        if axis == "y":
            paper = {(x, y) if y < v else (x, v - (y - v)) for x, y in paper}
        else:
            paper = {(x, y) if x < v else (v - (x - v), y) for x, y in paper}

    y_max = max(y for _, y in paper)
    x_max = max(x for x, _ in paper)
    out = [""]
    for y in range(y_max + 1):
        row = []
        for x in range(x_max + 1):
            row.append("@" if (x, y) in paper else " ")
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
