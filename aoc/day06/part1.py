import math

f = open("./input.txt")
inputtxt = f.read()
f.close()

def solve(input: str):
    rows = input.strip().split("\n")
    transform_col = lambda c: int(c) if c.isnumeric() else c
    matrix = [[transform_col(c) for c in r.strip().split()] for r in rows]
    problems = len(matrix[0])
    grand_total = 0
    for p in range(problems):
        nums = []
        for row in matrix:
            if row[p] == "*":
                grand_total += math.prod(nums)
                break
            if row[p] == "+":
                grand_total += sum(nums)
                break
            nums.append(row[p])
    return grand_total

print(solve(inputtxt))