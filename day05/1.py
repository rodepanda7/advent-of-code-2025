with open("big.txt", "r") as f:
    lines = f.read()

intervals_str, ids_str = lines.split('\n\n')
intervals = [(int(interval.split("-")[0]), int(interval.split("-")[1])) for interval in intervals_str.split()]
ids = [int(id) for id in ids_str.split()]

def is_fresh(id: int) -> bool:
   return any(start <= id <= end for start, end in intervals)

nr_fresh = 0
for id in ids:
    nr_fresh += is_fresh(id)

print(nr_fresh)