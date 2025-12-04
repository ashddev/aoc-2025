f = open("./input.txt")
inputtxt = f.read()
f.close()

def solve(input: str):
    matrix = list(map(list, input.strip().split("\n")))
    rows, cols = len(matrix), len(matrix[0])
    accessable_rolls = 0
    prev_accessible_rolls = -1
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
    while accessable_rolls != prev_accessible_rolls:
        prev_accessible_rolls = accessable_rolls
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "@":
                    num_adjacent_rolls = 0
                    for x, y in directions:
                        new_r, new_c = r + x, c + y
                        if 0 <= new_r < rows and 0 <= new_c < cols and matrix[new_r][new_c] == "@":
                            num_adjacent_rolls += 1
                    if num_adjacent_rolls < 4:
                        accessable_rolls += 1
                        matrix[r][c] = "."
    return accessable_rolls

print(solve(inputtxt))