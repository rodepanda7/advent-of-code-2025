from math import sqrt
from itertools import combinations

with open ("big.txt", "r") as f:
    boxes = [tuple(map(int, box.split(","))) for box in f.read().splitlines()]

BOXES = len(boxes)

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

max_circuit_size = 1
x1final, x2final = 0, 0

def update_circuits(circuit1, circuit2, size1, size2):
    for box, (circuit, size) in circuits.items():
        if circuit == circuit1 or circuit == circuit2:
            circuits[box] = (circuit1, size1 + size2)

while BOXES > max_circuit_size:
    print(BOXES, max_circuit_size)
    min_distance = min(distances.keys())
    box1, box2 = distances[min_distance]
    del distances[min_distance]

    circuit1, size1 = circuits[box1]
    circuit2, size2 = circuits[box2]

    if size1 == 1:
        max_circuit_size = max(max_circuit_size, size2 + 1)
        circuits[box1] = (circuit2, size2 + 1)
        update_circuits(circuit2, circuit1, 1, size2)
    elif size2 == 1:
        max_circuit_size = max(max_circuit_size, size1 + 1)
        circuits[box2] = (circuit1, size1 + 1)
        update_circuits(circuit1, circuit2, size1, 1)
    elif circuit1 != circuit2:
        max_circuit_size = max(max_circuit_size, size1 + size2)
        update_circuits(circuit1, circuit2, size1, size2)

    x1final, x2final = box1[0], box2[0]

print(x1final, x2final, x1final * x2final)