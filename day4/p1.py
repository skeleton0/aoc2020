import re
from aocd import get_data, submit

answer = 0
required_fields = frozenset(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
for passport in get_data(year=2020, day=4).split("\n\n"):
    fields = frozenset(re.findall("([a-z]{3}):", passport))
    if required_fields <= fields:
        answer += 1

print(answer)

