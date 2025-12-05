with open ("big.txt", "r") as f:
    grid = [line.strip() for line in f.readlines()]

HIGHT = len(grid)
WIDTH = len(grid[0])

# Returns True is a paper roll is accessible on position (y, x) and False otherwise
def is_accessible(y: int, x: int) -> bool:
    adjacent_rolls = 0
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            if i < 0 or i >= HIGHT or j < 0 or j >= WIDTH:
                continue
            if i == y and j == x:
                continue
            adjacent_rolls += grid[i][j] == '@'

    return adjacent_rolls < 4

positions = [(i, j) for i in range(HIGHT) for j in range(WIDTH)]
accessible_positions = list(filter(lambda x: grid[x[0]][x[1]] == '@' and is_accessible(x[0], x[1]), positions))

print(len(accessible_positions))