"""Day 17: Trick Shot

Algorithm:
    For y > 0 and vy > 0, the probe comes down at the velocity as it is shot up,
    so will inevitably be at some (x, 0). At the step immediately after y=0,
    the velocity will be -(vy + 1). Under these conditions, and for the probe
    to be in target, vy is maximized when -(vy + 1) = y_min.
"""
import sys


def parse_input(puzzle_input):
    _, _, raw_x, raw_y = puzzle_input.split()
    x_min, x_max = map(int, raw_x[2:-1].split(".."))
    y_min, y_max = map(int, raw_y[2:].split(".."))

    return (x_min, x_max, y_min, y_max)


def part_one(target_area):
    _, _, y_min, _ = target_area

    vy = -y_min - 1
    y = vy * (vy + 1) // 2
    return y
    # return (y_min *-~ y_min) >> 1


def part_two(target_area):
    x_min, x_max, y_min, y_max = target_area

    vx_min = 1
    while (vx_min * (vx_min + 1) / 2) < x_min:
        vx_min += 1
    vx_min -= 1

    # brute-force baby
    count = 0
    for vx_initial in range(vx_min, x_max + 1):
        for vy_initial in range(y_min, -y_min):
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
        assert part_two(parse_input(self.example)) == 112


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(puzzle))
    print("part 2:", part_two(puzzle))


if __name__ == "__main__":
    main()
