with open("big.txt", "r") as f:
    lines = f.read()

intervals_str, _ = lines.split('\n\n')
intervals = [(int(interval.split("-")[0]), int(interval.split("-")[1])) for interval in intervals_str.split()]
intervals.sort()

fresh_ids = 0
current = -1
for start, end in intervals:
    if current >= start:
        start = current + 1
    if start <= end:
        fresh_ids += end - start + 1
    current = max(current, end)

print(fresh_ids)