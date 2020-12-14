import re
from aocd import get_data

mem = {}
for line in get_data(year=2020, day=14).splitlines():
    if "mask" in line:
        mask = re.match(r"mask = ([\dX]{36})", line).group(1)
        or_mask = int(mask.replace('X', '0'), base=2)
        and_mask = int(mask.replace('X', '1'), base=2)
    else:
        match = re.match(r"mem\[(\d+)\] = (\d+)", line)
        value = int(match.group(2))
        value |= or_mask
        value &= and_mask
        mem[match.group(1)] = value

print(sum(mem.values()))
