import functools
import sys
import time


def stopwatch(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        before = time.perf_counter_ns()
        out = func(*args, **kwargs)
        after = time.perf_counter_ns()
        print(f"🕔 {after - before} ns", file=sys.stderr, flush=True)
        return out

    return wrapper
