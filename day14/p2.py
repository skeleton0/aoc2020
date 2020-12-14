import re
from aocd import get_data

mem = {}
for line in get_data(year=2020, day=14).splitlines():
    if "mask" in line:
        mask = re.match(r"mask = ([\dX]{36})", line).group(1)
        lsb_mask = list(mask)
        lsb_mask.reverse()
        or_mask = int(mask.replace('X', '0'), base=2)
    else:
        match = re.match(r"mem\[(\d+)\] = (\d+)", line)
        addr = int(match.group(1))
        value = int(match.group(2))
        addr |= or_mask
        addrs = {addr}
        for i, bit in enumerate(lsb_mask):
            if bit != 'X':
                continue
            new_addrs = set()
            floatmask = 2**i
            for a in addrs:
                new_addrs.add(a | floatmask)
                new_addrs.add(a & ~floatmask)
            addrs |= new_addrs

        for a in addrs:
            mem[a] = value

print(sum(mem.values()))
