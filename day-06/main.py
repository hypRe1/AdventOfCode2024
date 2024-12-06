import re

with open("day-06/input1.txt") as f:
    G = f.read().splitlines()

DIRS = {"^": (0, -1), ">": (1, 0), "<": (-1, 0), "v": (0, 1)}
ROTS = {(0, -1): (1, 0), (1, 0): (0, 1), (-1, 0): (0, -1), (0, 1): (-1, 0)}
p = re.compile("#")

obstacles = set()
x = (0, 0)
dx = (0, 0)
found = False
for j, row in enumerate(G):
    for m in p.finditer(row):
        obstacles.add((m.start(), j))

    if not found:
        for d in DIRS.keys():
            i = row.find(d)
            if i != -1:
                x = (i, j)
                dx = DIRS[d]
                found = True
                break


def q1() -> int:
    global x
    global dx
    seen = {x}
    states = set()
    n = 0
    while True:
        dy = ROTS[dx]
        y = (x[0] + dy[0], x[1] + dy[1])
        x = (x[0] + dx[0], x[1] + dx[1])

        if x[0] < 0 or x[0] >= len(G[0]) or x[1] < 0 or x[1] >= len(G):
            break

        if x in obstacles:
            dx = dy
            x = y

        seen.add(x)
        states.add((x, dx))

        z = y
        newstates = states.copy()
        path = []
        while True:
            y = (y[0] + dy[0], y[1] + dy[1])
            if y[0] < 0 or y[0] >= len(G[0]) or y[1] < 0 or y[1] >= len(G):
                break

            if y in obstacles:
                y = (x[0] - dy[0], x[1] - dy[1])
                dy = ROTS[dy]
                y = (x[0] + dy[0], x[1] + dy[1])

            if (y, dy) in newstates:
                print((z, dy), path)
                n += 1
                break

            path.append((y, dy))
            newstates.add((y, dy))

    return len(seen), n


def q2() -> int:
    return -1


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
