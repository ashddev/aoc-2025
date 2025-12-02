f = open("./input.txt")
inputtxt = f.read()
f.close()

def is_repeated_substring(num_str: str):
    l = len(num_str)
    for i in range(1, (l // 2) + 1):
        if l % i != 0:
            continue
        if num_str == num_str[:i] * (l // i):
            return True
    return False

def solve(input: str):
    transform = lambda x: tuple(map(int, x.split("-")))
    ranges = list(map(transform, input.strip().split(",")))
    result = 0
    for start, end in ranges:
        for num in range(start, end+1):
            result += num if is_repeated_substring(str(num)) else 0
    return result

print(solve(inputtxt))