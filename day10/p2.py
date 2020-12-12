import re
from aocd import get_data

def calculate_combinations(bits):
    possibilities = 2 ** bits
    if bits < 3:
        return possibilities

    valid_combos = 0
    for i in range(0, possibilities):
        if not re.search("000", format(i, f"0{bits}b")):
            valid_combos += 1
    return valid_combos

adapters = [int(i) for i in get_data(year=2020, day=10).splitlines()]

# Add outlet
adapters.append(0)
# Add built-in
adapters.append(max(adapters) + 3)
adapters.sort()

deltas = ''
for i, jolt_output in enumerate(adapters[1:], start=1):
    delta = jolt_output - adapters[i-1]
    if delta == 1:
        deltas += '1'
    elif delta == 3:
        deltas += '3'

combinations = 1
for group in re.findall("(1+)1", deltas):
    combinations *= calculate_combinations(len(group))

print(combinations)
