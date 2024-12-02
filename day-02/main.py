with open("day-02/input.txt") as f:
    inputData = f.readlines()


def valid(r: list[int]) -> bool:
    inc = (r[1] - r[0]) >= 1
    for i in range(len(r) - 1):
        diff = r[i + 1] - r[i]
        if (
            (not (1 <= abs(diff) <= 3))
            or (inc and diff <= -1)
            or (not inc and diff >= 1)
        ):
            return False
    return True


def q1() -> int:
    a = 0
    rs = []
    for line in inputData:
        rs.append(list(map(int, line.split(" "))))
    for r in rs:
        if valid(r):
            a += 1
    return a


def q2() -> int:
    a = 0
    rs = []
    for line in inputData:
        rs.append(list(map(int, line.split(" "))))
    r2s = []
    for r in rs:
        if valid(r):
            a += 1
        else:
            p = []
            for j in range(len(r)):
                n = r.copy()
                del n[j]
                p.append(n)
            r2s.append(tuple(p))

    for _rs in r2s:
        for r in _rs:
            if valid(r):
                a += 1
                break
    return a


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
