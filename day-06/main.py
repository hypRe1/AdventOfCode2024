import re

with open("day-06/input.txt") as f:
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


def main() -> None:
    global x
    global dx
    seen = {x}
    obstructions = set()
    while True:
        x = (x[0] + dx[0], x[1] + dx[1])

        if x in obstacles:
            x = (x[0] - dx[0], x[1] - dx[1])
            dx = ROTS[dx]
            continue

        if x[0] < 0 or x[0] >= len(G[0]) or x[1] < 0 or x[1] >= len(G):
            break

        if x not in obstructions:
            y = (x[0] - dx[0], x[1] - dx[1])
            dy = ROTS[dx]
            states = set()

            while True:
                y = (y[0] + dy[0], y[1] + dy[1])

                if y == x or y in obstacles:
                    y = (y[0] - dy[0], y[1] - dy[1])
                    dy = ROTS[dy]
                    continue

                if y[0] < 0 or y[0] >= len(G[0]) or y[1] < 0 or y[1] >= len(G):
                    break

                if (y, dy) in states:
                    obstructions.add(x)
                    break

                states.add((y, dy))
        seen.add(x)

    print(len(seen), len(obstructions))


if __name__ == "__main__":
    main()
