import argparse
import collections
import itertools
import timeit


def _fmt_time(sec):
    t = sec * 1000
    unit = "ms"
    if t < 1:
        t *= 1000
        unit = "μs"

    return f"{t:.2f} {unit}"


def day01(filename="data/01.txt"):
    with open(filename) as f:
        puzzle = [int(x) for x in f]

    part_one = (puzzle[1] > puzzle[0]) + (puzzle[2] > puzzle[1])
    ita, itb = itertools.tee(puzzle[2:])
    next(itb, None)

    part_two = 0
    window = collections.deque(puzzle[:3])
    for prev, curr in zip(ita, itb):
        part_one += prev < curr

        window.append(curr)
        part_two += curr > window.popleft()

    assert part_one == 1390
    assert part_two == 1457


def day02(filename="data/02.txt"):
    with open(filename) as f:
        puzzle = list(f)

    pos_one, depth_one = 0, 0
    pos_two, depth_two, aim = 0, 0, 0
    for line in puzzle:
        instruction, value = line.split()
        value = int(value)
        if instruction == "forward":
            pos_one += value
            pos_two += value
            depth_two += aim * value
        elif instruction == "down":
            depth_one += value
            aim += value
        elif instruction == "up":
            depth_one -= value
            aim -= value

    assert pos_one * depth_one == 1868935
    assert pos_two * depth_two == 1965970888


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw", action="store_true")
    args = parser.parse_args()

    if not args.raw:
        print("┌───────┬──────────────────┐")

    runtime = 0
    for i in range(1, 26):
        t = timeit.Timer(f"day{i:02}()", globals=globals())
        try:
            n, total_time = t.autorange()
        except NameError:
            break

        mean_time = total_time / n
        runtime += mean_time

        if args.raw:
            print(f"{i} {mean_time * 1000}")
        else:
            print(f"│ {i:5} │ {_fmt_time(mean_time):>9} {'(' + str(n) + ')':>6} │")

    if not args.raw:
        print("├───────┼──────────────────┤")
        print(f"│ total │ {_fmt_time(runtime):>9}        │")
        print("└───────┴──────────────────┘")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
