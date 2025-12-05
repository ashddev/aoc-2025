f = open("./input.txt")
inputtxt = f.read()
f.close()

def solve(input: str):
    ranges, ids = input.strip().split("\n\n")
    parsed_ranges = [tuple(map(int, r.split("-"))) for r in ranges.split("\n")]
    parsed_ids = list(map(int, ids.split("\n")))
    count = 0
    for id in parsed_ids:
        for start, end in parsed_ranges:
            if start <= id <= end:
                count += 1
                break
    return count

print(solve(inputtxt))