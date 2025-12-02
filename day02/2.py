with open ("big.txt", "r") as f:
    ranges = [(r.split("-")[0], r.split("-")[1]) for r in f.read().split(",")]

# Returns True if num is made of repeating string n multiple times
def n_repeats(n : str, num : str) -> bool:    
    while num != "":
        if num[:len(n)] != n:
            return False
        num = num[len(n):]
    return True

def is_valid(num : str) -> bool:
    for size in range(1, (len(num) // 2) + 1):
        if n_repeats(num[:size], num):
            return False
    return True

invalids = 0
for r in ranges:
    for num in range(int(r[0]), int(r[1]) + 1):
        if not is_valid(str(num)):
            invalids += num

print(invalids)