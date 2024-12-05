with open("day-05/input.txt") as f:
    a,b = map(lambda x: x.splitlines(), f.read().split("\n\n"))

G = set(map(lambda x: tuple(map(int, x.split("|"))), a))
O = list(map(lambda x: list(map(int, x.split(","))), b))

def q1() -> int:
    n = 0
    for p in O:
        for i in range(len(p)-1):
            if (p[i],p[i+1]) not in G:
                break
        else:
            n += p[len(p)//2]
    return n

def q2() -> int:
    n = 0
    for p in O:
        invalid = False
        unfixed = True
        while unfixed:
            unfixed = False
            for i in range(len(p)-1):
                if (p[i],p[i+1]) not in G:
                    p[i], p[i+1] = p[i+1], p[i]
                    invalid = True
                    unfixed = True
        if invalid:
            n += p[len(p)//2]
    return n

def main() -> None:
    print(q1())
    print(q2())

if __name__ == "__main__":
    main()
