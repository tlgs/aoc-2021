"""Day 10: Syntax Scoring"""
import sys


def syntax_error_score(lines):
    pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
    points = {"(": 3, "[": 57, "{": 1197, "<": 25137}
    total = 0
    for line in lines:
        stack = []
        for c in line:
            if c in points:
                stack.append(c)
            elif pairs[c] == stack[-1]:
                stack.pop()
            else:
                total += points[pairs[c]]
                break

    return total


def middle_autocomplete_score(lines):
    pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
    points = {"(": 1, "[": 2, "{": 3, "<": 4}
    scores = []
    for line in lines:
        stack = []
        for c in line:
            if c in points:
                stack.append(c)
            elif pairs[c] == stack[-1]:
                stack.pop()
            else:
                break

        else:
            total = 0
            while stack:
                total = total * 5 + points[stack.pop()]
            scores.append(total)

    scores.sort()
    return scores[len(scores) // 2]


class Test:
    example = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]

    def test_one(self):
        assert syntax_error_score(self.example) == 26397

    def test_two(self):
        assert middle_autocomplete_score(self.example) == 288957


def main():
    puzzle = [line.rstrip() for line in sys.stdin]

    print("part 1:", syntax_error_score(puzzle))
    print("part 2:", middle_autocomplete_score(puzzle))


if __name__ == "__main__":
    main()
