import re
from aocd import get_data

NORTH = 0
EAST = 90
SOUTH = 180
WEST = 270
headings = {'N': NORTH, 'E': EAST, 'S': SOUTH, 'W': WEST}

heading = EAST
x = 0
y = 0

def rotate(value):
    global heading
    heading = (heading + value) % 360

def translate(heading, value):
    global x, y
    if heading == NORTH:
        y -= value
    elif heading == EAST:
        x += value
    elif heading == SOUTH:
        y += value
    elif heading == WEST:
        x -= value

for line in get_data(year=2020, day=12).splitlines():
    match = re.match(r"([A-Z])(\d+)", line)
    action = match.group(1)
    value = int(match.group(2))
    if action in headings:
        translate(headings[action], value)
    elif action == 'F':
        translate(heading, value)
    elif action == 'L':
        rotate(-value)
    elif action == 'R':
        rotate(value)

print(abs(x) + abs(y))
