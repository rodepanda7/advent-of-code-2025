with open ("big.txt", "r") as f:
    rotations = [int(line[1:-1]) if line[0] == "R" else -1 * int(line[1:-1]) for line in f.readlines()]

position = 50
zeros = 0
for rotation in rotations:
    position = (position + rotation) % 100
    zeros += position == 0

print(zeros)