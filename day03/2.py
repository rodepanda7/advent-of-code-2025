with open ("big.txt", "r") as f:
    banks = [[int(battery) for battery in bank.strip()] for bank in f.readlines()]

BANK_LEN = len(banks[0])

def biggest_joltage(bank : list[int]) -> int:
    max_v = 0
    max_i = 0

    for i in range(11, -1, -1):
        max1 = max(bank[max_i:BANK_LEN - i])
        
        new_max_i = bank.index(max1)
        while new_max_i < max_i:
            new_max_i = bank[max_i:BANK_LEN - i].index(max1) + max_i
        
        max_i = new_max_i + 1
        max_v = max_v * 10 + max1
    
    return max_v

sum = 0
for bank in banks:
    sum += biggest_joltage(bank)

print(sum)