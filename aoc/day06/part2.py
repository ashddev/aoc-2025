from itertools import zip_longest

f = open("./input2.txt")
inputtxt = f.read()
f.close()

def cephalopod_math(nums: list):
    nums_strs = [str(n) for n in nums]
    max_length = len(max(nums_strs, key=lambda x: len(x)))
    print(nums_strs)
    print(max_length)
    nums_strs_padded = [s.ljust(max_length, "0") for s in nums_strs]
    print(nums_strs_padded)
    matrix = zip_longest(*[list(num) for num in nums_strs_padded])
    print(list(matrix))
    # cols = len(max(matrix, key=lambda x: len(x)))
    # new_nums = []
    # for c in range(cols):
    #     new_num = []
    #     for i, row in enumerate(matrix):
    #         last_el = len(row)-1-c
    #         if last_el < 0:
    #             continue
    #         new_num.append(row[last_el])
    #     print(new_num)
    #     new_nums.append(int("".join(new_num)))
    # return new_nums

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
                print(cephalopod_math(nums))
                # grand_total += math.prod(cephalopod_math(nums))
                break
            if row[p] == "+":
                print(cephalopod_math(nums))
                # grand_total += sum(cephalopod_math(nums))
                break
            nums.append(row[p])
    return grand_total

print(solve(inputtxt))