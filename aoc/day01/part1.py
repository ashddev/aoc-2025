f = open("./input.txt")
inputtxt = f.read()
f.close()

def solve(input: str):
    def transform(x):
        return int(x[1:]) * -1 if x[0] == "L" else int(x[1:])
    rotations = list(map(transform, input.strip().split("\n")))
    dial = 50
    count = 0
    for r in rotations:
        dial = (dial + r) % 100
        if dial == 0:
            count += 1
    return count

print(solve(inputtxt))