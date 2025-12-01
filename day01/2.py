with open ("big.txt", "r") as f:
    rotations = [int(line[1:-1]) if line[0] == "R" else -1 * int(line[1:-1]) for line in f.readlines()]

position = 50
zeros = 0
for rotation in rotations:
    tens_rot = rotation - 100 * (rotation // 100) if rotation > 0 else rotation - 100 * (rotation // 100 + 1)
    zeros += position != 0 and (tens_rot + position >= 100 or tens_rot + position <= 0)
    # Also update zeros for full cycles
    zeros += (rotation // 100) if rotation > 0 else -(rotation // 100 + 1)
    position = (position + rotation) % 100

print(zeros)