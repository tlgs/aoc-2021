"""Day 3: Binary Diagnostic"""
import collections
import itertools
import sys


def bits_per_line(stream):
    for line in stream:
        yield tuple(map(int, line))


def power_consumption(report):
    bit_counts = [0] * len(report[0])
    for bits in bits_per_line(report):
        for i, b in enumerate(bits):
            bit_counts[i] += b

    threshold = len(report) // 2
    gamma, epsilon = 0, 0
    for i, v in enumerate(bit_counts[::-1]):
        one_most_common = v > threshold
        gamma += one_most_common * 2 ** i
        epsilon += (not one_most_common) * 2 ** i

    return gamma * epsilon


def life_support_rating(report):
    counts = collections.defaultdict(int)
    for line in report:
        for v in itertools.accumulate(line):
            counts[v] += 1

    oxygen, co2 = "", ""
    for _, _ in enumerate(report[0]):
        if counts[oxygen + "1"] >= counts[oxygen + "0"]:
            oxygen += "1"
        else:
            oxygen += "0"

        ones = counts[co2 + "1"]
        zeroes = counts[co2 + "0"]
        if (ones >= 1 and ones < zeroes) or not zeroes:
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
