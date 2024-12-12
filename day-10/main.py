with open("day-10/input.txt") as f:
    inputData = f.read().split()

maxi = len(inputData[0])
maxj = len(inputData)

tiles = {}
starts = []
for j in range(maxj):
    for i in range(maxi):
        val = int(inputData[j][i])
        loc = i + j * 1j
        tiles[loc] = val
        if val == 0:
            starts.append(loc)


def q1() -> int:
    a = 0
    for start in starts:
        stack: list[complex] = [start]
        seen: set[complex] = set()
        while len(stack) > 0:
            loc = stack.pop()
            if tiles[loc] == 9:
                a += 1

            for dx in (-1 + 0j, 1 + 0j, -1j, 1j):
                new = loc + dx
                if new in seen:
                    continue

                newv = tiles.get(new)
                if newv is not None and newv == tiles[loc] + 1:
                    stack.append(new)
                    seen.add(new)
    return a


def q2() -> int:
    pass


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
