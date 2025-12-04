f = open("./input.txt")
inputtxt = f.read()
f.close()

def solve(input: str):
    transform = lambda x: list(map(int, list(x)))
    banks = list(map(transform, input.strip().split("\n")))
    total_joltage = 0
    for bank in banks:
        batteries = [0] * 2
        for i, joltage in enumerate(bank):
            if joltage > batteries[0] and i < len(bank) - 1:
                batteries[0] = joltage
                batteries[1] = 0
            elif joltage > batteries[1]:
                batteries[1] = joltage
        total_joltage += int("".join(map(str, batteries)))
    return total_joltage

print(solve(inputtxt))