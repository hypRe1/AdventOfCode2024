import itertools


def main() -> None:
    with open("day-12/input.txt") as f:
        inputData = f.read().splitlines()

    G = {}
    for j in range(len(inputData)):
        for i in range(len(inputData[0])):
            v = inputData[j][i]
            if G.get(v) is None:
                G[v] = {i + j * 1j}
            else:
                G[v].add(i + j * 1j)

    RG = {}
    for v, locs in G.items():
        regions = []
        seen = set()
        for l in locs:
            q = [l]
            region = set()
            seen_region = False
            while len(q) > 0:
                curr = q.pop(0)
                if curr in region:
                    continue
                if curr in seen:
                    seen_region = True
                    break
                region.add(curr)
                for dx in (1 + 0j, -1 + 0j, 0 + 1j, 0 - 1j):
                    new = curr + dx
                    if new not in locs or new in region or new in seen:
                        continue
                    q.append(new)
            if seen_region:
                continue
            seen |= region
            regions.append(region)
        RG[v] = regions

    a1 = 0
    a2 = 0
    for v, regions in RG.items():
        for r in regions:
            area = len(r)
            per = 4 * area
            sides = 0
            for x, y in itertools.combinations(r, r=2):
                if (x - y) in (1 + 0j, -1 + 0j, 0 + 1j, 0 - 1j):
                    per -= 2

            sides = 0
            for dx, dy in ((1, -1j), (1, 1j), (1j, -1), (1j, 1)):
                ups = set()
                upsides = []
                for x in r:
                    if x in ups:
                        continue
                    upside = set()
                    seen_upside = False
                    while True:
                        if x + dy in G.get(v) or x not in G.get(v):
                            break
                        curr = x
                        if x in ups:
                            seen_upside = True
                            break
                        upside.add(x)
                        x += dx
                    if seen_upside:
                        continue
                    if len(upside) == 0:
                        continue

                    upsides.append(upside)
                    ups |= upside
                sides += len(upsides)

            a2 += area * sides
            a1 += area * per
    return a1, a2


if __name__ == "__main__":
    main()
