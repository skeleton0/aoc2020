with open("input") as f:
    expenses = [int(line) for line in f]

for a in expenses:
    for b in expenses:
        for c in expenses:
            if (a + b + c) == 2020:
                print(a*b*c)
                exit()
