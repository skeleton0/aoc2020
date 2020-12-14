import math
from aocd import get_data

buses = [(int(bus), offset) for offset, bus in enumerate(get_data(year=2020, day=13).splitlines()[1].split(',')) if bus != 'x']

# Find the times where buses collide
collisions = []
for ts in range(buses[-1][1] + 1):
    collisions.append([])
    for bus, offset in buses:
        if (offset - ts) % bus == 0:
            collisions[ts].append(bus) 

# Find the highest LCM
hlcm = 0
hlcm_ts = 0
for ts, bus_ids in enumerate(collisions):
    lcm = math.prod(bus_ids)
    if lcm > hlcm:
        hlcm = lcm
        hlcm_ts = ts

common_mul = hlcm
while True:
    start = common_mul - hlcm_ts
    for bus_id, ts in buses:
        if (start + ts) % bus_id != 0:
            common_mul += hlcm
            break
    else:
        print(start)
        break
