import re

with open("day-04/input.txt") as f:
    inputData = f.read().splitlines()


def q1() -> int:
    n = 0

    # horizontal
    for line in inputData:
        n += len(re.findall("XMAS", line)) + len(re.findall("SAMX", line))

    # vertical
    v = ["".join([i[j] for i in inputData]) for j in range(len(inputData))]
    for line in v:
        n += len(re.findall("XMAS", line)) + len(re.findall("SAMX", line))

    # diag (complete mess)
    d = []
    for j in range(len(inputData)):
        diag = []
        for i in range(len(inputData[0])):
            if j >= len(inputData):
                break
            diag.append(inputData[j][i])
            j += 1
        d.append("".join(diag))
    for i in range(1, len(inputData[0])):
        diag = []
        for j in range(len(inputData)):
            if i >= len(inputData):
                break
            diag.append(inputData[j][i])
            i += 1
        d.append("".join(diag))
    for j in range(len(inputData)):
        diag = []
        for i in range(len(inputData[0])):
            if j < 0:
                break
            diag.append(inputData[j][i])
            j -= 1
        d.append("".join(diag))
    for js in range(1, len(inputData)):
        i = len(inputData[0]) - 1
        diag = []
        for j in range(js, len(inputData)):
            if i < 0 or j < 0:
                break
            diag.append(inputData[j][i])
            i -= 1
        d.append("".join(diag))
    for line in d:
        n += len(re.findall("XMAS", line)) + len(re.findall("SAMX", line))

    return n


def q2() -> int:
    n = 0
    for j in range(len(inputData) - 2):
        for i in range(len(inputData[0]) - 2):
            w1 = inputData[j][i] + inputData[j + 1][i + 1] + inputData[j + 2][i + 2]
            w2 = inputData[j + 2][i] + inputData[j + 1][i + 1] + inputData[j][i + 2]
            if w1 in ("MAS", "SAM") and w2 in ("MAS", "SAM"):
                n += 1
    return n


def main() -> None:
    print(q1())
    print(q2())


if __name__ == "__main__":
    main()
