f = open("./input.txt")
inputtxt = f.read()
f.close()

def solve(input: str):
    lines = [list(l) for l in input.strip().split("\n")]
    stack = set([lines.pop(0).index("S")])
    split_count = 0
    for l in lines:
        splitters = [i for i, x in enumerate(l) if x == "^"]
        if not splitters:
            continue
        for s in splitters:
            if s in stack:
                split_count += 1
                stack.remove(s)
                stack.add(s-1)
                stack.add(s+1)
    return split_count

print(solve(inputtxt))