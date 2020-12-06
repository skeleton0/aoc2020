from aocd import get_data

answer = 0
for group in get_data(year=2020, day=6).split("\n\n"):
    peoples_answers = [frozenset(person) for person in group.splitlines()]
    common = peoples_answers[0]
    for a in peoples_answers[1:]:
        common &= a
    answer += len(common)
    
print(answer)
