with open ("big.txt", "r") as f:
    grid = [list(row) for row in f.read().split("\n")]

beam_positions = [grid[0].index('S')]
grid[1][beam_positions[0]] = '1'

def update_grid_cel(i1, i2, j1, j2):
    if grid[i1][j1].isdigit():
        grid[i1][j1] = str(int(grid[i2][j2]) + int(grid[i1][j1]))
    else:
        grid[i1][j1] = grid[i2][j2]

for i in range(2, len(grid) - 1):
    new_beam_positions = []
    for j in range(len(grid[i])):
        if j not in beam_positions:
            continue
        if grid[i][j] != '^' and grid[i-1][j].isdigit():
            update_grid_cel(i, i-1, j, j)
            new_beam_positions.append(j)
        if grid[i][j] == '^' and grid[i-1][j].isdigit():
            update_grid_cel(i, i-1, j-1, j)
            update_grid_cel(i, i-1, j+1, j)
            new_beam_positions.append(j - 1)
            new_beam_positions.append(j + 1)

    beam_positions = new_beam_positions

timelines = 0
for num in grid[-2]:
    if num.isdigit():
        timelines += int(num)

print(timelines)