with open ("big.txt", "r") as f:
    grid = [list(row) for row in f.read().split("\n")]

beam_positions = [grid[0].index('S')]
splits = 0

for i in range(1, len(grid) - 1):
    new_beam_positions = []
    for j in range(len(grid[i])):
        if j not in beam_positions:
            continue
        if grid[i][j] == '^' and grid[i-1][j] == '|':
            splits += 1
            grid[i][j-1] = '|'
            grid[i][j+1] = '|'
            new_beam_positions.append(j - 1)
            new_beam_positions.append(j + 1)
        if grid[i][j] == '.' and (grid[i-1][j] == '|' or grid[i-1][j] == 'S'):
            new_beam_positions.append(j)
            grid[i][j] = '|'

    beam_positions = new_beam_positions

print(splits)