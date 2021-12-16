"""Day 2: Dive!"""
import operator
import sys


def extracted(commands):
    for command in commands:
        i, v = command.split()
        yield i, int(v)


def run_course_one(commands):
    pos, depth = 0, 0
    for instruction, value in extracted(commands):
        if instruction == "forward":
            pos += value
        elif instruction == "down":
            depth += value
        elif instruction == "up":
            depth -= value

    return pos, depth


def run_course_two(commands):
    pos, depth, aim = 0, 0, 0
    for instruction, value in extracted(commands):
        if instruction == "forward":
            pos += value
            depth += aim * value
        elif instruction == "down":
            aim += value
        elif instruction == "up":
            aim -= value

    return pos, depth


class Test:
    example = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]

    def test_one(self):
        assert run_course_one(self.example) == (15, 10)

    def test_two(self):
        assert run_course_two(self.example) == (15, 60)


def main():
    puzzle = list(sys.stdin)

    print("part 1:", operator.mul(*run_course_one(puzzle)))
    print("part 2:", operator.mul(*run_course_two(puzzle)))


if __name__ == "__main__":
    main()
