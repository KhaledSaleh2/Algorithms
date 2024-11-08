import sys

lines = sys.stdin.readlines()
num_instances = int(lines[0].strip())
line_num = 1
for _ in range(num_instances):
    num_items, capacity = map(int, lines[line_num].strip().split())
    line_num += 1
    if num_items == 0:
        print('0')
        continue
    items = []
    for _ in range(num_items):
        pair = lines[line_num].strip().split()
        line_num += 1
        items.append((int(pair[0]), int(pair[1])))
    dp_row = [0] * (capacity + 1)
    for num in range(capacity + 1):
        dp_row[num] = 0 if num - items[0][0] < 0 else items[0][1]
    for index in range(1, num_items):
        for j in range(capacity, items[index][0] - 1, -1):
            added_val = dp_row[j - items[index][0]] + items[index][1]
            dp_row[j] = max(dp_row[j], added_val)
    print(dp_row[capacity])
