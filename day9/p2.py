from aocd import get_data

data = [int(i) for i in get_data(year=2020, day=9).splitlines()]
for i, val in enumerate(data[25:], start=25):
    found = False
    for j in data[i-25:i]:
        for k in data[i-25:i]:
            if j != k and j+k == val:
                found = True
                break
        if found:
            break
    if not found:
        invalid_number = val
        break

for i, start in enumerate(data):
    total = start
    for j, end in enumerate(data[i+1:], start=i+1):
        total += end
        if total > invalid_number:
            break
        elif total == invalid_number:
            sequence = data[i:j+1]
            print(min(sequence) + max(sequence))
            exit()
