import re
from math import prod

with open("day-03/input.txt") as f:
    inputData = f.read()


def q1() -> int:
    a = 0
    for match in re.findall(pattern=r"mul\(\d+,\d+\)", string=inputData):
        s = match.find("(")
        e = match.find(")")
        a += prod(map(int, match[s + 1 : e].split(",")))
    return a


def q2() -> int:
    active = True
    last = 0
    a = 0
    for match in re.findall(pattern=r"mul\(\d+,\d+\)", string=inputData):
        current = inputData.index(match)
        domatches = re.findall(
            pattern=r"do\(\)|don't\(\)", string=inputData[last:current]
        )
        if len(domatches) != 0:
            active = domatches[-1] == "do()"
        s = match.find("(")
        e = match.find(")")
        if active:
            a += prod(map(int, match[s + 1 : e].split(",")))

        last = current
    return a


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
