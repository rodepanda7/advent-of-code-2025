from math import prod

with open("big.txt", "r") as f:
    lines = f.readlines()
numlines, ops = lines[0:-1], list(filter(lambda x: x != ' ', lines[-1].strip()))
numslines = [[int(num) for num in nums.split()] for nums in numlines]

# Transpose numslines
numslines = list(map(list, zip(*numslines)))
result = 0
for i, numsline in enumerate(numslines):
    match ops[i]:
        case '+':
            result += sum(numsline)
        case '*':
            result += prod(numsline)

print(result)