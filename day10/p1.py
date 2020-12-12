from aocd import get_data

adapters = [int(i) for i in get_data(year=2020, day=10).splitlines()]
# Add outlet
adapters.append(0)
# Add built-in
adapters.append(max(adapters) + 3)
adapters.sort()

delta1 = 0
delta3 = 0
for i, jolt_output in enumerate(adapters[1:], start=1):
    delta = jolt_output - adapters[i-1]
    if delta == 1:
        delta1 += 1
    elif delta == 3:
        delta3 += 1

print(delta1 * delta3)

