"""Day 3: Binary Diagnostic"""
import itertools
import sys


def power_consumption(report):
    bit_counts = [0] * len(report[0])
    for line in report:
        for i, v in enumerate(line):
            if v == "1":
                bit_counts[i] += 1

    gamma, epsilon = 0, 0
    for i, _ in enumerate(bit_counts):
        gamma <<= 1
        epsilon <<= 1
        if bit_counts[i] > len(report) // 2:
            gamma += 1
        else:
            epsilon += 1

    return gamma * epsilon


def life_support_rating(report):
    counts = {}
    for line in report:
        for v in itertools.accumulate(line):
            counts[v] = counts.get(v, 0) + 1

    oxygen, co2 = "", ""
    for _, _ in enumerate(report[0]):
        if counts.get(oxygen + "1", 0) >= counts.get(oxygen + "0", 0):
            oxygen += "1"
        else:
            oxygen += "0"

        if counts.get(co2 + "1", sys.maxsize) < counts.get(co2 + "0", sys.maxsize):
            co2 += "1"
        else:
            co2 += "0"

    return int(oxygen, 2) * int(co2, 2)


class Test:
    example = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010",
    ]

    def test_one(self):
        assert power_consumption(self.example) == 198

    def test_two(self):
        assert life_support_rating(self.example) == 230


def main():
    puzzle = [line.strip() for line in sys.stdin]

    print("part 1:", power_consumption(puzzle))
    print("part 2:", life_support_rating(puzzle))


if __name__ == "__main__":
    main()
