import re
from aocd import get_data

rules = {}
for rule in get_data(year=2020, day=7).splitlines():
    parent_bag = re.match("(\w+ \w+) bag", rule).group(1)
    child_bags = re.findall("(\d+) (\w+ \w+) bag", rule)
    rules[parent_bag] = child_bags

def count_bags(bag):
    total_count = 1
    for count, bag in rules[bag]:
        total_count += int(count) * count_bags(bag)
    return total_count

# -1 Because we don't count the shiny gold bag itself
print(count_bags("shiny gold") - 1)
