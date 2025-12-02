f = open("./input.txt")
inputtxt = f.read()
f.close()

def solve(input: str):
    transform = lambda x: tuple(map(int, x.split("-")))
    ranges = list(map(transform, input.strip().split(",")))
    result = 0
    for start, end in ranges:
        for num in range(start, end+1):
            num_str = str(num)
            if len(num_str) % 2 != 0:
                continue
            elif num_str[:len(num_str)//2] == num_str[len(num_str)//2:]:
                    result += num
    return result

print(solve(inputtxt))