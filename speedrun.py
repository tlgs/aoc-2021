import argparse
import collections
import itertools
import sys
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


def day03(filename="data/03.txt"):
    with open(filename) as f:
        puzzle = [line.strip() for line in f]

    bit_counts = [0] * len(puzzle[0])
    for line in puzzle:
        for i, v in enumerate(line):
            if v == "1":
                bit_counts[i] += 1

    gamma, epsilon = 0, 0
    for ones in bit_counts:
        gamma <<= 1
        epsilon <<= 1
        if ones > len(puzzle) // 2:
            gamma += 1
        else:
            epsilon += 1

    trie = {}
    for line in puzzle:
        for v in itertools.accumulate(line):
            trie[v] = trie.get(v, 0) + 1

    o2, co2 = "", ""
    for _ in puzzle[0]:
        if trie.get(o2 + "1", 0) >= trie.get(o2 + "0", 0):
            o2 += "1"
        else:
            o2 += "0"

        if trie.get(co2 + "1", sys.maxsize) < trie.get(co2 + "0", sys.maxsize):
            co2 += "1"
        else:
            co2 += "0"

    assert gamma * epsilon == 741950
    assert int(o2, 2) * int(co2, 2) == 903810


def day04(filename="data/04.txt"):
    with open(filename) as f:
        raw_numbers, *raw_boards = f.read().split("\n\n")

    numbers = [int(x) for x in raw_numbers.split(",")]
    flat_boards = [[int(x) for x in board.split()] for board in raw_boards]

    class Board:
        def __init__(self, flat_board):
            self.positions = dict((v, i) for i, v in enumerate(flat_board))
            self.marked = set()

        def check_win(self, idx, n):
            row, col = divmod(idx, 5)
            hz = set(range(row * 5, row * 5 + 5)) <= self.marked
            vt = set(range(col, 25, 5)) <= self.marked

            return sum(self.positions.keys()) * n if hz or vt else None

        def update(self, n):
            if n not in self.positions:
                return None

            idx = self.positions.pop(n)
            self.marked.add(idx)

            return self.check_win(idx, n)

    boards = [Board(fb) for fb in flat_boards]
    playing = set(i for i, _ in enumerate(boards))
    scores = []
    while len(scores) != len(boards):
        for n in numbers:
            for i, board in enumerate(boards):
                if i not in playing:
                    continue

                if (s := board.update(n)) is not None:
                    playing.remove(i)
                    scores.append(s)

    part_one, *_, part_two = scores

    assert part_one == 38594
    assert part_two == 21184


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
