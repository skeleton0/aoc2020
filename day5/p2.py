from aocd import get_data, submit

seats = []
for seat in get_data(year=2020, day=5).splitlines():
    rows = list(range(0, 128))
    columns = list(range(0, 8))
    row_spec = seat[:7]
    column_spec = seat[7:]

    for c in row_spec:
        middle = len(rows) // 2
        if len(rows) == 2:
            row = rows[0] if c == 'F' else rows[1]
        else:
            rows = rows[:middle] if c == 'F' else rows[middle:]
    for c in column_spec:
        middle = len(columns) // 2
        if len(columns) == 2:
            column = columns[0] if c == 'L' else columns[1]
        else:
            columns = columns[:middle] if c == 'L' else columns[middle:]

    seat_id = row * 8 + column
    seats.append(seat_id)

# Find the missing seat ID
seats.sort()
before = seats[0]
for seat in seats[1:]:
    if seat - before != 1:
        print(before + 1)
        break
    before = seat
