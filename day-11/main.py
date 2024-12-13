from functools import lru_cache

with open("day-11/input.txt") as f:
    inputData = list(map(int, f.read().split()))

ns = inputData.copy()


@lru_cache(maxsize=None)
def transform_n(n: int) -> tuple[int]:
    nstr = str(n)
    nl = len(nstr)
    if n == 0:
        return (1,)
    elif nl % 2 == 0:
        return (int(nstr[: nl // 2]), int(nstr[nl // 2 :]))
    else:
        return (n * 2024,)


@lru_cache(maxsize=None)
def transform(stones: tuple[int], times: int) -> tuple:
    if times == 0:
        return stones

    if len(stones) == 1:
        return transform(transform_n(stones[0]), times - 1)

    newstones = []
    for stone in stones:
        newstones += list(transform((stone,), times))
    return tuple(newstones)


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
    # [blink() for _ in range(25)]
    # return len(ns)
    print(len(transform(tuple(ns), 75)))


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
    print(q1())
    # print(q2())


if __name__ == "__main__":
    main()
