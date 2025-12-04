with open ("big.txt", "r") as f:
    banks = [[int(battery) for battery in bank.strip()] for bank in f.readlines()]

def biggest_joltage(bank : list[int]) -> int:
    max1 = max(bank)
    i1 = bank.index(max1)
    
    if i1 == len(bank) - 1:
        max2 = max1
        max1 = max(bank[:i1])
    else:
        max2 = max(bank[i1+1:])
    
    return max1 * 10 + max2

sum = 0
for bank in banks:
    sum += biggest_joltage(bank)

print(sum)