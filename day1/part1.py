with open("input") as f:
    expenses = [int(line) for line in f]

for a in expenses:
    for b in expenses:
        if (a + b) == 2020:
            print(a*b)
            exit()
