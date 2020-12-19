from aocd import get_data

history = {}
for t, startnum in enumerate(get_data(year=2020, day=15).split(',')):
    last = int(startnum)
    history[last] = t

staged = 0
for t in range(len(history), 30000000):
    if staged in history:
        staging = t - history[staged]
        history[staged] = t
        staged = staging
    else:
        history[staged] = t
        staged = 0

for val, t in history.items():
    if t == 29999999:
        print(val)
        break
