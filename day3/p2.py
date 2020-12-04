from aocd import get_data, submit

data = get_data(year=2020, day=3)

paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
answer = 1
for x_incr, y_incr in paths:
    trees = 0
    x = x_incr
    for line in data.splitlines()[y_incr::y_incr]:
        if line[x] == "#":
            trees += 1
        x += x_incr
        if x >= len(line):
            x = x - len(line)
    answer *= trees

submit(answer, part='b', year=2020, day=3)
