f = open("./input2t.txt")
inputtxt = f.read()
f.close()

def solve(input: str):
    lines = [list(l) for l in input.strip().split("\n")]
    start = lines.pop(0).index("S")
    stack = set([start])
    timelines = [0] * len(lines[0])
    timelines[start] = 1
    for l in lines:
        splitters = [i for i, x in enumerate(l) if x == "^"]
        if not splitters:
            continue
        for s in splitters:
            if s in stack:
                stack.remove(s)
                stack.add(s-1)
                stack.add(s+1)
                timelines[s-1] += 1
                timelines[s+1] += 1
    return sum(timelines)

print(solve(inputtxt))