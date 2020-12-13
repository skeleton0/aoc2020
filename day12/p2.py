import re
from aocd import get_data

waypoint_x = 10
waypoint_y = -1
ship_x = 0
ship_y = 0

def rotate_waypoint(direction, value):
    global waypoint_x, waypoint_y
    for _ in range(0, value // 90):
        new_x = waypoint_x
        new_y = waypoint_y
        if direction == 'R':
            new_x = -waypoint_y if waypoint_y > 0 else abs(waypoint_y)
            new_y = waypoint_x
        elif direction == 'L':
            new_x = waypoint_y
            new_y = -waypoint_x if waypoint_x > 0 else abs(waypoint_x)
        waypoint_x = new_x
        waypoint_y = new_y

def translate_waypoint(heading, value):
    global waypoint_x, waypoint_y
    if heading == 'N':
        waypoint_y -= value
    elif heading == 'E':
        waypoint_x += value
    elif heading == 'S':
        waypoint_y += value
    elif heading == 'W':
        waypoint_x -= value

def translate_ship(value):
    global ship_x, ship_y
    ship_x += waypoint_x * value
    ship_y += waypoint_y * value

for line in get_data(year=2020, day=12).splitlines():
    match = re.match(r"([A-Z])(\d+)", line)
    action = match.group(1)
    value = int(match.group(2))
    if action == 'F':
        translate_ship(value)
    elif action in ['R', 'L']:
        rotate_waypoint(action, value)
    else:
        translate_waypoint(action, value)

print(abs(ship_x) + abs(ship_y))
