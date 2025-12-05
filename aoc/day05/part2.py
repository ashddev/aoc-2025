f = open("./input.txt")
inputtxt = f.read()
f.close()

def solve(input: str):
    ranges, _ = input.strip().split("\n\n")
    parsed_ranges = [tuple(map(int, r.split("-"))) for r in ranges.split("\n")]
    parsed_ranges.sort(key=lambda x: x[0])
    count = 0
    max_end = 0
    for i, r in enumerate(parsed_ranges):
        s, e = r
        if i == 0:
            count += e - s + 1
            max_end = e
            continue
        if s > max_end:
            count += e - s + 1
            max_end = e
        else:
            if e > max_end:
                count += e - max_end
                max_end = e
    return count

print(solve(inputtxt))