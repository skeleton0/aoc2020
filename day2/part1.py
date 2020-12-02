import re
from aocd import get_data, submit

answer = 0
for line in get_data(year=2020, day=2).splitlines():
    match = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
    lower = int(match.group(1))
    upper = int(match.group(2))
    char = match.group(3)
    passwd = match.group(4)

    count = passwd.count(char)
    if lower <= count <= upper:
        answer += 1

submit(answer, part='a', year=2020, day=2)
