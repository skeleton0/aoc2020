from aocd import get_data

history = [int(start_num) for start_num in get_data(year=2020, day=15).split(',')]
while len(history) < 2020:
    for i in range(len(history)-2, -1, -1):
        if history[i] == history[-1]:
            history.append(len(history) - 1 - i)
            break
    else:
        history.append(0)

print(history[-1])
