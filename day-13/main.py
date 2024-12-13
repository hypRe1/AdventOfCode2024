import itertools
import re

import numpy as np

with open("day-13/input.txt") as f:
    inputData = f.read()


def nums(inp: str) -> list[int]:
    return list(map(int, re.findall("\\d+", inp)))


def main() -> None:
    a1 = 0
    a2 = 0
    for a, b, c in map(lambda x: map(nums, x.splitlines()), inputData.split("\n\n")):
        for x, y in itertools.product(range(101), repeat=2):
            if a[0] * x + b[0] * y == c[0] and a[1] * x + b[1] * y == c[1]:
                a1 += x * 3 + y
                break

        c = [z + 10000000000000 for z in c]
        res = list(map(round, np.linalg.inv([[a[0], b[0]], [a[1], b[1]]]).dot(c)))
        if res[0] < 0 or res[1] < 0:
            continue
        if (
            a[0] * res[0] + b[0] * res[1] == c[0]
            and a[1] * res[0] + b[1] * res[1] == c[1]
        ):
            a2 += res[0] * 3 + res[1]
    print(a1, a2)


if __name__ == "__main__":
    main()
