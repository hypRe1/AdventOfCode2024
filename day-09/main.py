with open("day-09/input1.txt") as f:
    inputData = f.read()


def q1() -> int:
    idn = []
    g = True
    n = 0
    for c in inputData:
        if g:
            idn += int(c) * [str(n)]
            n += 1
        else:
            idn += int(c) * [-1]

        g = not g

    while -1 in idn:
        index = idn.index(-1)
        idn[index] = idn.pop()

    return sum([i * int(d) for i, d in enumerate(idn)])


def q2() -> int:
    idn = []
    ms = []
    g = True
    n = 0
    for c in inputData:
        if int(c) > 0:
            ms.append(int(c))
            if g:
                idn.append(int(n))
                n += 1
            else:
                idn.append(-1)

        g = not g

    s = 0
    vi = -1
    over = False
    while -1 in idn:
        # print(s)
        try:
            if s > (vi % len(idn)):
                vi -= 1
                s = 0
                print("yayaya")
                continue
            index = idn.index(-1, s)
        except ValueError:
            vi -= 1
            if abs(vi) > len(idn):
                over = True
                break
            while idn[vi] == -1:
                vi -= 1
                if abs(vi) > len(idn):
                    over = True
                    break
            s = 0
            continue
        if over:
            break
        if idn[vi] == -1:
            vi -= 1
            s = 0
            continue

        diff = ms[index] - ms[vi]
        if diff >= 0:
            print(idn[vi], index, vi % len(idn))
            idn[index] = idn.pop(vi)
            ms[index] = ms.pop(vi)
            if diff > 0:
                ms.insert(index + 1, diff)
                idn.insert(index + 1, -1)
            vi = -1
            if abs(vi) > len(idn):
                over = True
                break
            while idn[vi] == -1:
                vi -= 1
                if abs(vi) > len(idn):
                    over = True
                    break
            if over:
                break

            i = vi % len(idn)

            print(", ".join([str(n) * m for n, m in zip(idn, ms)]))
            s = 0

        else:
            s = index + 1

    a = 0
    i = 0
    for n, m in zip(idn, ms):
        if n == -1:
            continue
        for _ in range(m):
            a += n * i
            i += 1

    return a


def main() -> None:
    # print(q1())
    print(q2())


if __name__ == "__main__":
    main()
