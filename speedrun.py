import argparse
import collections
import itertools
import statistics
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
    part_two = 0
    window = collections.deque(puzzle[:3])
    for prev, curr in itertools.pairwise(puzzle[2:]):
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

    part_one = pos_one * depth_one
    part_two = pos_two * depth_two

    assert part_one == 1868935
    assert part_two == 1965970888


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

    part_one = gamma * epsilon
    part_two = int(o2, 2) * int(co2, 2)

    assert part_one == 741950
    assert part_two == 903810


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


def day05(filename="data/05.txt"):
    segments = []
    with open(filename) as f:
        for line in f:
            raw_fst, raw_snd = line.split(" -> ")
            fst = tuple(int(x) for x in raw_fst.split(","))
            snd = tuple(int(x) for x in raw_snd.split(","))
            segments.append((fst, snd))

    counts1 = collections.defaultdict(int)
    counts2 = collections.defaultdict(int)
    for start, end in segments:
        x1, y1, x2, y2 = *start, *end
        dx = ((x2 - x1) > 0) - ((x2 - x1) < 0)
        dy = ((y2 - y1) > 0) - ((y2 - y1) < 0)

        for i, j in zip(
            range(x1, x2 + dx, dx) if dx else itertools.repeat(x1),
            range(y1, y2 + dy, dy) if dy else itertools.repeat(y1),
        ):
            counts2[(i, j)] += 1

            if not dx or not dy:
                counts1[(i, j)] += 1

    part_one = sum(v > 1 for v in counts1.values())
    part_two = sum(v > 1 for v in counts2.values())

    assert part_one == 7468
    assert part_two == 22364


def day06(filename="data/06.txt"):
    with open(filename) as f:
        ages = [int(x) for x in f.read().split(",")]

    parts = []
    school = collections.Counter(ages)
    for runs in (80, 176):
        for _ in range(runs):
            resets = school.get(0, 0)
            for i in range(8):
                school[i] = school.get(i + 1, 0)

            school[8] = resets
            school[6] += resets

        parts.append(school.total())

    part_one, part_two = parts

    assert part_one == 360268
    assert part_two == 1632146183902


def day07(filename="data/07.txt"):
    with open(filename) as f:
        crabs = [int(x) for x in f.read().split(",")]

    xtilde = round(statistics.median(crabs))
    part_one = sum(abs(y - xtilde) for y in crabs)

    xbar = statistics.mean(crabs)
    cost = []
    for x in map(int, [xbar - 0.5, xbar + 0.5]):
        v = sum((abs(y - x) * (abs(y - x) + 1)) // 2 for y in crabs)
        cost.append(v)

    part_two = min(cost)

    assert part_one == 343441
    assert part_two == 98925151


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw", action="store_true")
    args = parser.parse_args()

    runs = []
    for i in range(1, 26):
        t = timeit.Timer(f"day{i:02}()", globals=globals())
        try:
            n, total_time = t.autorange()
        except NameError:
            break

        mean_time = total_time / n
        runs.append((mean_time, n))

    if not args.raw:
        print("┌───────┬───────────┬──────┐")
        print("│   day │ mean time │ runs │")
        print("├───────┼───────────┼──────┤")

        for i, (mt, n) in enumerate(runs, start=1):
            print(f"│ {i:5} │ {_fmt_time(mt):>9} │ {n:>4} │")

        print("├───────┼───────────┼──────┘")
        print(f"│ total │ {_fmt_time(sum(t for t, _ in runs)):>9} │")
        print("└───────┴───────────┘")

    else:
        for i, (mt, _) in enumerate(runs, start=1):
            print(f"{i} {mt * 1000}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
