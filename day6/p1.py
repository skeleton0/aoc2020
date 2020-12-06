import re
from aocd import get_data

answer = 0
for group in get_data(year=2020, day=6).split("\n\n"):
    answer += len(frozenset(re.findall("[a-z]", group)))

print(answer)
