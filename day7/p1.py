import re
from aocd import get_data

rules = {}
for rule in get_data(year=2020, day=7).splitlines():
    bags = re.findall("(\w+ \w+) bag", rule)
    if "no other" in bags:
        bags.pop()
    rules[bags[0]] = bags[1:]

def can_contain_shiny_gold(bag):
    for b in rules[bag]:
        if b == "shiny gold" or can_contain_shiny_gold(b):
            return True
    return False

answer = 0
for b in rules:
    if can_contain_shiny_gold(b):
        answer += 1

print(answer)
