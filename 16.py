"""Day 16: Packet Decoder

Notes:
    `import pytest` adds ~140ms to runtime
"""
import math
import sys

import pytest


def hex_to_bin(x):
    table = str.maketrans({c: f"{int(c, base=16):04b}" for c in "0123456789ABCDEF"})
    return x.translate(table)


def parse_packet(x):
    version, x = int(x[:3], base=2), x[3:]
    type_id, x = int(x[:3], base=2), x[3:]

    if type_id == 4:
        value = []
        while True:
            lead, g, x = int(x[0]), x[1:5], x[5:]
            value.append(g)
            if not lead:
                break

        packet_length = 6 + 5 * len(value)
        value = int("".join(value), base=2)
        return version, packet_length, value

    else:
        length_type_id, x = int(x[0]), x[1:]

        subpacket_versions = []
        subpacket_values = []
        if length_type_id == 0:
            total_length, x = int(x[:15], base=2), x[15:]
            to_go = total_length
            while to_go:
                packet_version, packet_length, v = parse_packet(x)
                x = x[packet_length:]
                to_go -= packet_length
                subpacket_versions.append(packet_version)
                subpacket_values.append(v)

            total_length += 22

        else:
            n, x = int(x[:11], base=2), x[11:]
            total_length = 0
            for _ in range(n):
                packet_version, packet_length, v = parse_packet(x)
                x = x[packet_length:]
                total_length += packet_length
                subpacket_versions.append(packet_version)
                subpacket_values.append(v)

            total_length += 18

        match type_id:
            case 0:
                value = sum(subpacket_values)
            case 1:
                value = math.prod(subpacket_values)
            case 2:
                value = min(subpacket_values)
            case 3:
                value = max(subpacket_values)
            case 5:
                a, b = subpacket_values
                value = a > b
            case 6:
                a, b = subpacket_values
                value = a < b
            case 7:
                a, b = subpacket_values
                value = a == b
            case _:
                raise ValueError

        return version + sum(subpacket_versions), total_length, value


def part_one(message):
    version_sum, _, _ = parse_packet(hex_to_bin(message))
    return version_sum


def part_two(message):
    _, _, value = parse_packet(hex_to_bin(message))
    return value


class Test:
    @pytest.mark.parametrize(
        "test_input,expected",
        [
            ("8A004A801A8002F478", 16),
            ("620080001611562C8802118E34", 12),
            ("C0015000016115A2E0802F182340", 23),
            ("A0016C880162017C3686B18A3D4780", 31),
        ],
    )
    def test_one(self, test_input, expected):
        assert part_one(test_input) == expected

    @pytest.mark.parametrize(
        "test_input,expected",
        [
            ("C200B40A82", 3),
            ("04005AC33890", 54),
            ("880086C3E88112", 7),
            ("CE00C43D881120", 9),
            ("D8005AC2A8F0", 1),
            ("F600BC2D8F", 0),
            ("9C005AC2F8F0", 0),
            ("9C0141080250320F1802104A08", 1),
        ],
    )
    def test_two(self, test_input, expected):
        assert part_two(test_input) == expected


def main():
    puzzle = sys.stdin.read()

    print("part 1:", part_one(puzzle))
    print("part 2:", part_two(puzzle))


if __name__ == "__main__":
    main()
