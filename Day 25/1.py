with open('input25.txt', 'r') as f:
    lines = [x.strip() for x in f if x.strip()]

locks, keys = [], []
for i in range(0, len(lines), 7):
    group = [sum(1 for x in col if x == ('#' if lines[i] == '#####' else '.')) for col in zip(*lines[i+1:i+7])]
    (locks if lines[i] == '#####' else keys).append(tuple(5 - x if lines[i] != '#####' else x for x in group))

print(sum(all(l[j] + k[j] <= 5 for j in range(5)) for l in locks for k in keys))