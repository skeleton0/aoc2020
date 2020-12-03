from aocd import get_data, submit

data = get_data(year=2020, day=3)

x_incr = 3
x = x_incr
answer = 0
for line in data.splitlines()[1:]:
    if line[x] == "#":
        answer += 1
    x += x_incr
    if x >= len(line):
        x = x - len(line)

submit(answer, part='a', year=2020, day=3)
