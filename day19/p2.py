import re
from aocd import get_data

data = get_data(year=2020, day=19)
rules = {rule_no : rule for rule_no, rule in re.findall(r"(\d+): ([^\n]+)", data)}

def compile_rule(rule_expr):
    compiled_rule = ""
    for e in rule_expr.split(" "):
        if e.isdecimal():
            compiled_subrule = compile_rule(rules[e])
            if '|' in compiled_subrule:
                compiled_rule += f"(?:{compiled_subrule})"
            else:
                compiled_rule += compiled_subrule
        elif match := re.fullmatch('"([a-z])"', e):
            compiled_rule += match.group(1)
        elif e == '|':
            compiled_rule += '|'
    return compiled_rule

compiled_rule = f"((?:{compile_rule(rules['42'])}){{2,}})((?:{compile_rule(rules['31'])})+)"
answer = 0
for line in data.split("\n\n")[1].splitlines():
    if match := re.fullmatch(compiled_rule, line):
        if len(re.findall(compile_rule(rules['42']), match.group(1))) > len(re.findall(compile_rule(rules['31']), match.group(2))):
            answer += 1

print(answer)
