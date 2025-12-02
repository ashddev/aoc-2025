f = open("./input.txt")
inputtxt = f.read()
f.close()

def solve(input: str):
    transform = lambda x: (x[0], int(x[1:]))
    rotations = list(map(transform, input.strip().split("\n")))
    dial = 50
    count = 0
    for direction, value in rotations:
        delta = 1 if direction == "R" else -1
        for _ in range(value):
            dial = (dial + delta) % 100 
            if dial == 0: 
                count += 1
    return count

print(solve(inputtxt))