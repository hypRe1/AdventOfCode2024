# This is an auto-generated template

with open("day-11/input.txt") as f:
    inputData = list(map(int, f.read().split()))

ns = inputData.copy()


def blink():
    global ns
    new = []
    for n in ns:
        nstr = str(n)
        nl = len(nstr)
        if n == 0:
            new.append(1)
        elif nl % 2 == 0:
            new.append(int(nstr[: nl // 2]))
            new.append(int(nstr[nl // 2 :]))
        else:
            new.append(n * 2024)
    ns = new.copy()


def q1() -> int:
    [blink() for _ in range(25)]
    return len(ns)


def q2() -> int:
    global ns
    ns = inputData.copy()
    nsc = ns.copy()
    a = 0
    for n in nsc:
        ns = [n]
        [blink() for _ in range(75)]
        a += len(ns)
        print(a)
    return a


def main() -> None:
    # print(q1())
    print(q2())


if __name__ == "__main__":
    main()
