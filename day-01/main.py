with open("day-01/input.txt") as f:
    inputData = f.readlines()


def parse() -> tuple[list[int], list[int]]:
    xs: list[int] = []
    ys: list[int] = []
    for l in inputData:
        pair = tuple(map(int, l.strip().split()))
        xs.append(pair[0])
        ys.append(pair[1])
    return xs, ys


def q1() -> int:
    xs, ys = map(sorted, parse())
    return sum([abs(xs[i] - ys[i]) for i in range(len(xs))])


def q2() -> int:
    xs, ys = parse()
    return sum([x * ys.count(x) for x in xs])


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
