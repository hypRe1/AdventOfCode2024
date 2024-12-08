import itertools

with open("day-08/input.txt") as f:
    inputData = f.read().splitlines()

antennas = {}
for j, l in enumerate(inputData):
    for i, c in enumerate(l):
        if c.isalnum():
            if antennas.get(c) is None:
                antennas[c] = {complex(real=i, imag=j)}
            else:
                antennas[c] |= {complex(real=i, imag=j)}


def q1() -> int:
    locs = set()
    maxx = len(inputData[0])
    maxy = len(inputData)
    for cs in antennas.values():
        for x, y in itertools.combinations(cs, 2):
            d = y - x
            for z in (y + d, x - d):
                if 0 <= z.real < maxx and 0 <= z.imag < maxy:
                    locs.add(z)

    return len(locs)


def q2() -> int:
    locs = set()
    maxx = len(inputData[0])
    maxy = len(inputData)
    for cs in antennas.values():
        for x, y in itertools.combinations(cs, 2):
            d = y - x
            for i in range(100):
                for z in (y + d * i, x - d * i):
                    if 0 <= z.real < maxx and 0 <= z.imag < maxy:
                        locs.add(z)

    return len(locs)


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
