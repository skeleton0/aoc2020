import re
from aocd import get_data, submit

answer = 0
for line in get_data(year=2020, day=2).splitlines():
    match = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
    pos_a = int(match.group(1)) - 1
    pos_b = int(match.group(2)) - 1
    char = match.group(3)
    passwd = match.group(4)
    # If the character occurs in one of the positions exclusively (XOR)
    if (passwd[pos_a] == char) ^ (passwd[pos_b] == char):
        answer += 1

submit(answer, part='b', year=2020, day=2)
