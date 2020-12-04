import re
from aocd import get_data, submit

answer = 0
required_fields = frozenset(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
for passport in get_data(year=2020, day=4).split("\n\n"):
    fields = dict(re.findall("([a-z]{3}):(\S+)", passport))
    # Check that the passport contains all the required fields
    if not (required_fields <= frozenset(fields)):
        continue
    # Validate field values
    valid = True
    for field, lower, upper in [("byr", 1920, 2002), ("iyr", 2010, 2020), ("eyr", 2020, 2030)]:
        valid &= re.fullmatch("\d{4}", fields[field]) and lower <= int(fields[field]) <= upper

    match = re.fullmatch("(\d+)(cm|in)", fields["hgt"])
    if not match:
        continue
    valid &= match.group(2) == "cm" and 150 <= int(match.group(1)) <= 193 or match.group(2) == "in" and 59 <= int(match.group(1)) <= 76
    valid &= re.fullmatch("#[0-9a-f]{6}", fields["hcl"]) != None
    valid &= re.fullmatch("amb|blu|brn|gry|grn|hzl|oth", fields["ecl"]) != None
    valid &= re.fullmatch("\d{9}", fields["pid"]) != None
    
    if valid:
        answer += 1

print(answer)

