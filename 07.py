"""Day 6: The Treachery of Whales

Algorithm:
    In part 1, the fuel cost function f(k) = ∑ |k - xi|,
  where k is the "convergence" position in consideration and xi is the ith point.
  We are looking to find the value of k that minimizes f.
    df / dk = ∑ sign(k - xi), and this function equals zero only when
  the number of positive numbers equals the number of negative numbers;
  this happens when k = median{x1, x2, ..., xN}.
    See <https://math.stackexchange.com/a/1024462> for a good overview.

    The second part involves realizing that the **individual** cost function
  f(n) = Tn, where Tn is the nth _triangular number_; note that Tn = n * (n + 1) / 2.
  Important to undertand that here n is the distance between points: |k - xi|.
  See <https://en.wikipedia.org/wiki/Triangular_number>.
    Then, we have f(k) = ∑ (|k - xi| * (|k - xi| + 1)) / 2, and
  df / dk = ∑ sign(k - xi) / 2 + (k - x).

    ∑ sign(k - xi) / 2 + (k - x) = 0
          ∑ sign(k - xi) / 2 + k = ∑ xi
      N * k + ∑ sign(k - xi) / 2 = ∑ xi
                               k = ∑ xi / N - (∑ sign(k - xi) / N) / 2

    At this point we have that (∑ xi) / N is the sample mean x̄.
  While another term persists that depends on k, we can observe that
  this term is **bounded**: ∑ sign(k - xi) is maximally N and minimally -N.
    We conclude then that:
            x̄ - 1/2 <= k <= x̄ + 1/2
"""
import statistics
import sys


def fuel_linear(crabs):
    x = round(statistics.median(crabs))
    return sum(abs(y - x) for y in crabs)


def fuel_triangular(crabs):
    xbar = statistics.mean(crabs)

    cost = []
    for x in map(int, [xbar - 0.5, xbar + 0.5]):
        v = sum((abs(y - x) * (abs(y - x) + 1)) // 2 for y in crabs)
        cost.append(v)

    return min(cost)


class Test:
    example = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

    def test_one(self):
        assert fuel_linear(self.example) == 37

    def test_two(self):
        assert fuel_triangular(self.example) == 168


def main():
    puzzle = [int(x) for x in sys.stdin.read().split(",")]

    print("part 1:", fuel_linear(puzzle))
    print("part 2:", fuel_triangular(puzzle))


if __name__ == "__main__":
    main()
