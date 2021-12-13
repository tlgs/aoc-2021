import collections
import itertools
import timeit


def _fmt_time(sec):
    time = sec * 1000
    unit = "ms"
    if time < 1:
        time *= 1000
        unit = "μs"

    return f"{int(time)} {unit}"


def day01(filename="data/01.txt"):
    with open(filename) as f:
        puzzle = [int(x) for x in f]

    # pre-compute first two values
    part_one = sum(prev < curr for prev, curr in zip(puzzle[:2], puzzle[1:3]))

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


def main():
    runtime = 0
    for i in range(1, 26):
        t = timeit.Timer(f"day{i:02}()", globals=globals())
        try:
            n, total_time = t.autorange()
        except NameError:
            continue

        avg = total_time / n
        print(_fmt_time(avg))

        runtime += avg

    print("-" * 6)
    print(_fmt_time(runtime))


if __name__ == "__main__":
    main()
