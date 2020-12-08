import re
from aocd import get_data

data = get_data(year=2020, day=8)
program = []
for line in data.splitlines():
    match = re.match(r"(\w{3}) ((?:\+|-)\d+)", line)
    program.append((match.group(1), int(match.group(2))))

ptr = 0
acc = 0
history = set()
while True:
    op, arg = program[ptr]
    if ptr in history:
        print(acc)
        break
    else:
        history.add(ptr)
        
    if op == "nop":
        ptr += 1
    elif op == "acc":
        acc += arg
        ptr += 1
    elif op == "jmp":
        ptr += arg
