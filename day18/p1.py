import re
from aocd import get_data

def evalexpr(expr):
    components = []
    parenthesis = 0
    for i, c in enumerate(expr):
        if parenthesis > 0:
            if c == '(':
                parenthesis += 1
            elif c == ')':
                parenthesis -= 1
        else:
            if re.match(r"[\d+*]", c):
                components.append(c)
            elif c == '(':
                components.append(str(evalexpr(expr[i+1:])))
                parenthesis += 1
            elif c == ')':
                break
    # Return evaluated components
    evaluation = 0
    op = None
    for c in components:
        if c.isdecimal():
            if op in [None, '+']:
                evaluation += int(c)
            else:
                evaluation *= int(c)
        elif c in ['+', '*']:
            op = c
    return evaluation

answer = 0
for expr in get_data(year=2020, day=18).splitlines():
    answer += evalexpr(expr)
print(answer)
