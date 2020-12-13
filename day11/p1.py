import copy
from aocd import get_data

seats = []
for row in get_data(year=2020, day=11).splitlines():
    seats.append([c for c in row])

height = len(seats)
width = len(seats[0])

def adjacent_occupied(y, x):
    adjacent_coords = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for offset_y, offset_x in adjacent_coords:
        test_y = y + offset_y
        test_x = x + offset_x
        if 0 <= test_y < height and 0 <= test_x < width and seats[test_y][test_x] == '#':
            count += 1
    return count

new_seats = copy.deepcopy(seats)
while True:
    changed = False
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            occupied = adjacent_occupied(i, j)
            if seat == 'L' and not occupied:
                new_seats[i][j] = '#'
                changed = True
            elif seat == '#' and occupied >= 4:
                new_seats[i][j] = 'L'
                changed = True
    seats = copy.deepcopy(new_seats)
    if not changed:
        break

answer = 0
for row in seats:
    for seat in row:
        if seat == '#':
            answer += 1
print(answer)
