import re
from aocd import get_data, submit

data = get_data(year=2020, day=8)
program = []
for line in data.splitlines():
    match = re.match(r"(\w{3}) ((?:\+|-)\d+)", line)
    program.append((match.group(1), int(match.group(2))))

for i in range(0,len(program)):
    if program[i][0] != "jmp":
        continue
    program[i] = ("nop", program[i][1])
    ptr = 0
    history = set()
    acc = 0
    while True:
        instruct, value = program[ptr]
        if ptr in history:
            break
        else:
            history.add(ptr)
            
        if instruct == "nop":
            ptr += 1
        elif instruct == "acc":
            acc += value
            ptr += 1
        elif instruct == "jmp":
            ptr += value
        if ptr >= len(program) or ptr < 0:
            print(acc)
            exit()
    # Revert modifications to program
    program[i] = ("jmp", program[i][1])
