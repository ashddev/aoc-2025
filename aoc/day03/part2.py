f = open("./input.txt")
inputtxt = f.read()
f.close()

def solve(input: str):
    transform = lambda x: list(map(int, list(x)))
    banks = list(map(transform, input.strip().split("\n")))
    total_joltage = 0
    for bank in banks:
        batteries = [0] * 12
        for position, joltage in enumerate(bank):
            for i, recorded in enumerate(batteries):
                if joltage > recorded and position < len(bank) - (11-i):
                    batteries[i] = joltage
                    for reset in range(i+1, 12):
                        batteries[reset] = 0
                    break
        total_joltage += int("".join(map(str, batteries)))
    return total_joltage

print(solve(inputtxt))