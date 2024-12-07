import itertools

with open("day-07/input.txt") as f:
    inputData = f.read().splitlines()


def main():
    a1 = 0
    a2 = 0
    for line in inputData:
        i = line.find(":")
        t = int(line[:i])
        ns = line[i + 1 :].strip().split()
        for ops in itertools.product((0, 1), repeat=len(ns) - 1):
            nums = list(map(int, ns.copy()))
            for op in ops:
                n = nums.pop(1)
                if op:
                    nums[0] += n
                else:
                    nums[0] *= n
            if nums[0] == t:
                a1 += t
                break

        for ops in itertools.product((0, 1, 2), repeat=len(ns) - 1):
            nums = list(map(int, ns.copy()))
            for op in ops:
                n = nums.pop(1)
                if op == 0:
                    nums[0] += n
                elif op == 1:
                    nums[0] *= n
                elif op == 2:
                    nums[0] = nums[0] * 10 ** len(str((n))) + n
            if nums[0] == t:
                a2 += t
                break
    print(a1, a2)


if __name__ == "__main__":
    main()
