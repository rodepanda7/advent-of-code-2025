from math import prod

with open("big.txt", "r") as f:
    lines = f.readlines()

numslines, ops = lines[0:-1], list(filter(lambda x: x != ' ', lines[-1].strip()))
# Transpose numslines
numslines = list(map(list, zip(*numslines)))

# maps [' ', '1', '2'] to 12
def nums_map(column: list[str]) -> int | None:
    if all(char == ' ' or char == '\n' for char in column):
        return None
    
    number = 0
    for num in column:
        if not num.isdigit():
            continue
        number = number * 10 + int(num)
    
    return number

numslines = list(map(nums_map, numslines))

nice_numlines = [[]]
index = 0
for num in numslines:
    if num is not None:
        nice_numlines[index].append(num)
    else:
        index += 1
        nice_numlines.append([])
nice_numlines.pop()  # remove last empty list

result = 0
for i, numsline in enumerate(nice_numlines):
    match ops[i]:
        case '+':
            result += sum(numsline)
        case '*':
            result += prod(numsline)

print(result)