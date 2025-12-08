from math import sqrt, prod
from itertools import combinations

with open ("big.txt", "r") as f:
    boxes = [tuple(map(int, box.split(","))) for box in f.read().splitlines()]

def distance(box1, box2):
    return sqrt((box1[0]-box2[0])**2 + (box1[1]-box2[1])**2 + (box1[2]-box2[2])**2)

# key: distance, value: (box1, box2)
distances = {}
for box1, box2 in combinations(boxes, 2):
    distances[distance(box1, box2)] = (box1, box2)

# key : box, value: (index of circuit, size of circuit)
circuits = {}
for index, box in enumerate(boxes):
    circuits[box] = (index, 1)

def update_circuits(circuit1, circuit2, size1, size2):
    for box, (circuit, size) in circuits.items():
        if circuit == circuit1 or circuit == circuit2:
            circuits[box] = (circuit1, size1 + size2)

for i in range(1000):
    min_distance = min(distances.keys())
    box1, box2 = distances[min_distance]
    del distances[min_distance]

    circuit1, size1 = circuits[box1]
    circuit2, size2 = circuits[box2]

    if size1 == 1:
        circuits[box1] = (circuit2, size2 + 1)
        update_circuits(circuit2, circuit1, 1, size2)
    elif size2 == 1:
        circuits[box2] = (circuit1, size1 + 1)
        update_circuits(circuit1, circuit2, size1, 1)
    elif circuit1 != circuit2:
        update_circuits(circuit1, circuit2, size1, size2)

print(circuits.values())

max3 = sorted(set((size for _, size in circuits.values())), reverse=True)[:3]
print(prod(max3))