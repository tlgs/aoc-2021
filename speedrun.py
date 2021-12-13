import collections
import itertools
import timeit


def day01():
    with open("data/01.txt") as f:
        puzzle = [int(x) for x in f]

    # pre-compute first two values
    out_one = sum(prev < curr for prev, curr in zip(puzzle[:2], puzzle[1:3]))

    ita, itb = itertools.tee(puzzle[2:])
    next(itb, None)

    out_two = 0
    window = collections.deque(puzzle[:3])
    for prev, curr in zip(ita, itb):
        out_one += prev < curr

        window.append(curr)
        out_two += curr > window.popleft()

    assert out_one == 1390
    assert out_two == 1457


def format_time(sec):
    time = sec * 1000
    unit = "ms"
    if time < 1:
        time *= 1000
        unit = "μs"

    return f"{int(time)} {unit}"


def main():
    runtime = 0
    for i in range(1, 26):
        t = timeit.Timer(f"day{i:02}()", globals=globals())
        try:
            n, total_time = t.autorange()
        except NameError:
            continue

        avg = total_time / n
        print(format_time(avg))

        runtime += avg

    print("-" * 6)
    print(format_time(runtime))


if __name__ == "__main__":
    main()
