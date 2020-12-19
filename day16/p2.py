import re
from aocd import get_data

class FieldSpec:
    def __init__(self, name, bounds):
        self.name = name
        self.bounds = bounds

    def is_compliant_value(self, v):
        for a, b in self.bounds:
            if a <= v <= b:
                return True
        return False

data = get_data(year=2020, day=16)

fieldspecs = [] 
for name, a1, b1, a2, b2 in re.findall(r"([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)", data):
    fieldspec = FieldSpec(name, [(int(a1), int(b1)), (int(a2), int(b2))])
    fieldspecs.append(fieldspec)

valid_tickets = []
for ticket in re.findall(r"[\d,]+", data.split("nearby tickets:")[1]):
    ticket_fields = []
    for f in ticket.split(','):
        field = int(f)
        for fieldspec in fieldspecs:
            if fieldspec.is_compliant_value(field):
                ticket_fields.append(field)
                break
        else:
            break
    else:
        valid_tickets.append(ticket_fields)

# Find the common field specs for each field position
ordered_common_specs = []
for field_pos in range(len(fieldspecs)):
    common_specs = {spec.name for spec in fieldspecs}
    for ticket in valid_tickets:
        matching_specs = set()
        for spec in fieldspecs:
            if spec.is_compliant_value(ticket[field_pos]):
                matching_specs.add(spec.name)
        common_specs &= matching_specs
    ordered_common_specs.append(common_specs)

while True:
    changed = False
    for i in ordered_common_specs:
        if len(i) == 1:
            continue
        for j in ordered_common_specs:
            if len(j) == 1:
                i -= j
                changed = True
                if len(i) == 1:
                    break
    if not changed:
        break

# Change sets into list
ordered_specs = [name for specs in ordered_common_specs for name in specs]

# Calculate answer
answer = 1
my_ticket = [int(field) for field in re.search(r"your ticket:\n([^\n]+)", data).group(1).split(',')]
for i, field in enumerate(ordered_specs):
    if "departure" in field:
        answer *= my_ticket[i]

print(answer)
