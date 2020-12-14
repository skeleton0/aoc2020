from aocd import get_data

data = get_data(year=2020, day=13).splitlines()
earliest_time = int(data[0])
buses = [int(bus) for bus in data[1].split(',') if bus != 'x']

best_bus_id = buses[0]
lowest_wait_time = buses[0]
for bus in buses:
    r = earliest_time % bus
    wait_time = bus - r
    if r == 0:
        best_bus_id = bus
        lowest_wait_time = 0
        break
    elif wait_time < lowest_wait_time:
        best_bus_id = bus
        lowest_wait_time = wait_time

print(best_bus_id * lowest_wait_time)

