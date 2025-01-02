from collections import deque

with open('input09.txt') as f:
    rawinput = f.read().strip()  # Strip any trailing whitespace or newline characters

lengths = [int(num) for num in rawinput if num.isdigit()]  # Filter out non-digit characters

filled_grid = deque()
moved_grid = deque()
gaps = deque()

cur_pos = 0
for i, num in enumerate(lengths):
    if i % 2 == 0:
        filled_grid.append([i // 2, cur_pos, num])
    else:
        if num > 0:
            gaps.append([cur_pos, num])
    cur_pos += num

while True:
    gap_pos, gap_len = gaps.popleft()
    file_id, file_pos, file_len = filled_grid.pop()
    if gap_pos > file_pos:
        filled_grid.append([file_id, file_pos, file_len])
        break
    if gap_len > file_len:
        moved_grid.append([file_id, gap_pos, file_len])
        gaps.appendleft([gap_pos + file_len, gap_len - file_len])
    elif gap_len == file_len:
        moved_grid.append([file_id, gap_pos, file_len])
    else:
        moved_grid.append([file_id, gap_pos, gap_len])
        filled_grid.append([file_id, file_pos, file_len - gap_len])

final_grid = filled_grid + moved_grid
answer = sum(num * (start * length + (length * (length - 1)) // 2) for num, start, length in final_grid)  # (start) + (start+1) + ... + (start+length-1)
print(answer)
