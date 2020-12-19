import re
from aocd import get_data

data = get_data(year=2020, day=16)

rules = []
for a1, b1, a2, b2 in re.findall(r"(\d+)-(\d+) or (\d+)-(\d+)", data):
    rules.extend([(int(a1), int(b1)), (int(a2), int(b2))])

invalid_fields = []
for ticket in re.findall(r"[\d,]+", data.split("nearby tickets:")[1]):
    for f in ticket.split(','):
        field = int(f)
        for lower, upper in rules:
            if lower <= field <= upper:
                break
        else:
            invalid_fields.append(field)

print(sum(invalid_fields))

