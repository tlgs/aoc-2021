"""Day 17: Trick Shot

Algorithm:
    Ugly brute-force.
"""
import sys


def parse_input(puzzle_input):
    _, _, raw_x, raw_y = puzzle_input.split()
    x_min, x_max = map(int, raw_x[2:-1].split(".."))
    y_min, y_max = map(int, raw_y[2:].split(".."))

    return (x_min, x_max, y_min, y_max)


def f(v, s):
    if s == 0:
        return v
    return f(v, s - 1) + (v - s)


def part_one(target_area):
    x_min, x_max, y_min, y_max = target_area

    vx_min = 1
    while (vx_min * (vx_min + 1) / 2) < x_min:
        vx_min += 1
    vx_min -= 1

    # brute-force baby
    ans = 0
    for vx_initial in range(vx_min, x_max + 1):
        for vy_initial in range(y_min, 400):
            x, y = 0, 0
            vx, vy = vx_initial, vy_initial
            candidate = 0
            while x <= x_max and y >= y_min:
                if x >= x_min and y <= y_max:
                    ans = max(ans, candidate)
                    break
                x += vx
                y += vy

                if vx > 0:
                    vx -= 1
                elif vx < 0:
                    vx += 1

                vy -= 1
                candidate = max(candidate, y)

    return ans


def part_two(target_area):
    x_min, x_max, y_min, y_max = target_area

    vx_min = 1
    while (vx_min * (vx_min + 1) / 2) < x_min:
        vx_min += 1
    vx_min -= 1

    # brute-force baby
    count = 0
    for vx_initial in range(vx_min, x_max + 1):
        for vy_initial in range(y_min, 500):
            x, y = 0, 0
            vx, vy = vx_initial, vy_initial
            while x <= x_max and y >= y_min:
                if x >= x_min and y <= y_max:
                    count += 1
                    break
                x += vx
                y += vy

                vy -= 1

                if vx > 0:
                    vx -= 1
                elif vx < 0:
                    vx += 1

    return count


class Test:
    example = """\
target area: x=20..30, y=-10..-5
"""

    def test_one(self):
        assert part_one(parse_input(self.example)) == 45

    def test_two(self):
        assert True
        # assert part_two(self.example) == expected


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(puzzle))
    print("part 2:", part_two(puzzle))


if __name__ == "__main__":
    main()
