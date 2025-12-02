with open ("big.txt", "r") as f:
    ranges = [(r.split("-")[0], r.split("-")[1]) for r in f.read().split(",")]

def is_valid(num : str) -> bool:
    if len(num) % 2 != 0:
        return True

    mid = len(num) // 2
    left, right = num[:mid], num[mid:]
    return left != right

invalids = 0
for r in ranges:
    for num in range(int(r[0]), int(r[1]) + 1):
        if not is_valid(str(num)):
            invalids += num

print(invalids)