"""Day 4: Giant Squid"""
import sys


def parse_bingo(stream):
    numbers = [int(x) for x in next(stream).split(",")]
    next(stream)  # skip first blank line

    boards = []
    curr = []
    for i, line in enumerate(stream, start=1):
        if i % 6:
            curr += [int(x) for x in line.split()]
        else:
            boards.append(curr)
            curr = []

    return (numbers, *boards)


def score_winner(numbers, *boards):
    marked = [set() for _ in boards]
    for i, n in enumerate(numbers):
        for j, board in enumerate(boards):
            try:
                idx = board.index(n)
                marked[j].add(idx)
            except ValueError:
                continue

            if i < 4:
                continue

            row, col = divmod(idx, 5)
            horizontal = all(x in marked[j] for x in range(row * 5, row * 5 + 5))
            vertical = all(x in marked[j] for x in range(col, 25, 5))
            if horizontal or vertical:
                return sum(board[k] for k in range(25) if k not in marked[j]) * n

    raise RuntimeError


def score_loser(numbers, *boards):
    playing = set(i for i, _ in enumerate(boards))
    marked = [set() for _ in boards]
    for i, n in enumerate(numbers):
        for j, board in enumerate(boards):
            if j not in playing:
                continue

            try:
                idx = board.index(n)
                marked[j].add(idx)
            except ValueError:
                continue

            if i < 4:
                continue

            row, col = divmod(idx, 5)
            horizontal = all(x in marked[j] for x in range(row * 5, row * 5 + 5))
            vertical = all(x in marked[j] for x in range(col, 25, 5))
            if horizontal or vertical:
                playing.remove(j)
                if not playing:
                    return sum(board[k] for k in range(25) if k not in marked[j]) * n

    raise RuntimeError


class Test:
    # fmt: off
    example = (
        [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1],  # noqa: E501
        [22, 13, 17, 11, 0, 8, 2, 23, 4, 24, 21, 9, 14, 16, 7, 6, 10, 3, 18, 5, 1, 12, 20, 15, 19],  # noqa: E501
        [3, 15, 0, 2, 22, 9, 18, 13, 17, 5, 19, 8, 7, 25, 23, 20, 11, 10, 24, 4, 14, 21, 16, 12, 6],  # noqa: E501
        [14, 21, 17, 24, 4, 10, 16, 15, 9, 19, 18, 8, 23, 26, 20, 22, 11, 13, 6, 5, 2, 0, 12, 3, 7],  # noqa: E501
    )
    # fmt: on

    def test_one(self):
        assert score_winner(*self.example) == 4512

    def test_two(self):
        assert score_loser(*self.example) == 1924


def main():
    puzzle = parse_bingo(sys.stdin)

    print("part 1:", score_winner(*puzzle))
    print("part 2:", score_loser(*puzzle))


if __name__ == "__main__":
    main()
