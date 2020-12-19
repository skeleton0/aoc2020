import itertools
from aocd import get_data

def count_neighbours(point, pocket):
    px, py, pz, pw = point
    count = 0
    cartesian_product = set(itertools.product([-1,0,1], repeat=4))
    cartesian_product.remove((0,0,0,0))
    for nx, ny, nz, nw in cartesian_product:
        if (px+nx, py+ny, pz+nz, pw+nw) in pocket:
            count += 1
    return count

pocket = set()
for y, line in enumerate(get_data(year=2020, day=17).splitlines()):
    for x, state in enumerate(line):
        if state == '#':
            pocket.add((x,y,0,0))

for _ in range(6):
    # Calculate search space
    lower_bound = [0,0,0,0]
    upper_bound = [0,0,0,0]
    
    for cube in pocket:
        for i, value in enumerate(cube):
            lower_bound[i] = min(lower_bound[i], value)
            upper_bound[i] = max(upper_bound[i], value)
    # Create ranges for search space
    ranges = []
    for i in range(4):
        ranges.append(list(range(lower_bound[i]-1, upper_bound[i]+2)))

    new_pocket = pocket.copy()
    for point in itertools.product(*ranges):
        neighbours = count_neighbours(point, pocket)
        if point in pocket and not (2 <= neighbours <= 3):
            new_pocket.remove(point)
        elif point not in pocket and neighbours == 3:
            new_pocket.add(point)
    pocket = new_pocket

print(len(pocket))
