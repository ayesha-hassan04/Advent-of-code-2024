import datetime
import re

from collections import defaultdict

# Read input from 'input.txt'
with open('input15.txt', 'r') as f:
    inp = f.read()

# Split the input into grid and directions
parts = inp.split("\n\n")
lines = parts[0].split("\n")

# Function to expand grid tiles
def expand(c):
    if c == "O":
        return "[]"
    elif c == "@":
        return "@."
    else:
        return c + c

# Expanding the grid
lines = ["".join(expand(c) for c in l) for l in lines]
#print("\n".join(lines))

# Dimensions of the expanded grid
m = len(lines)
n = len(lines[0])

# Create a grid (using defaultdict to simplify handling of missing cells)
grid = defaultdict(lambda: defaultdict(lambda: "!"))
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        grid[i][j] = c

# Directions corresponding to <, >, ^, v
dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
chardirs = {"<": 1, ">": 0, "^": 2, "v": 3}

# Function to check if a move is valid
def check_move(d, i, j, already_checked):
    if (i, j) in already_checked:
        return already_checked[(i, j)]
    already_checked[(i, j)] = True
    if grid[i][j] == "#":
        already_checked[(i, j)] = False
    elif grid[i][j] == ".":
        already_checked[(i, j)] = True
    elif grid[i][j] == "@":
        already_checked[(i, j)] = check_move(d, i + d[0], j + d[1], already_checked)
    elif grid[i][j] == "[":
        already_checked[(i, j)] = check_move(d, i + d[0], j + d[1], already_checked) and check_move(d, i, j + 1, already_checked)
    elif grid[i][j] == "]":
        already_checked[(i, j)] = check_move(d, i + d[0], j + d[1], already_checked) and check_move(d, i, j - 1, already_checked)
    return already_checked[(i, j)]

# Function to commit the move
def commit_move(d, i, j, already_committed):
    if (i, j) in already_committed:
        return
    already_committed.add((i, j))
    if grid[i][j] == "#":
        return
    elif grid[i][j] == ".":
        return
    elif grid[i][j] == "[":
        commit_move(d, i + d[0], j + d[1], already_committed)
        commit_move(d, i, j + 1, already_committed)
        grid[i + d[0]][j + d[1]] = grid[i][j]
        grid[i][j] = "."
    elif grid[i][j] == "]":
        commit_move(d, i + d[0], j + d[1], already_committed)
        commit_move(d, i, j - 1, already_committed)
        grid[i + d[0]][j + d[1]] = grid[i][j]
        grid[i][j] = "."
    elif grid[i][j] == "@":
        commit_move(d, i + d[0], j + d[1], already_committed)
        grid[i + d[0]][j + d[1]] = grid[i][j]
        grid[i][j] = "."

# Find initial robot position
robot_pos = (0, 0)
for i in range(m):
    for j in range(n):
        if grid[i][j] == "@":
            robot_pos = (i, j)

# Directions to move (from input)
for dirchar in parts[1]:
    if dirchar == "\n":
        continue
    d = dirs[chardirs[dirchar]]  # Get the direction tuple
    if check_move(d, robot_pos[0], robot_pos[1], {}):
        commit_move(d, robot_pos[0], robot_pos[1], set())  # Commit the move
        robot_pos = (robot_pos[0] + d[0], robot_pos[1] + d[1])  # Update robot position

# Calculate GPS sum for boxes
result = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == "[":
            # Calculate the GPS coordinate for the box
            result += 100 * i + j

# Print the final result
print("Final GPS sum:", result)

# Read the input from 'input.txt' file
def read_input(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data

# Part a: Solving the puzzle
def a(data):
    grid, moves = data.split("\n\n")
    wall = set()
    boxes = set()
    pos = None
    for i, line in enumerate(grid.splitlines()):
        width = len(line)
        for j, c in enumerate(line):
            if c == "#":
                wall.add(j + i*1j)
            elif c == "O":
                boxes.add(j + i*1j)
            elif c == "@":
                pos = j + i*1j
    height = i + 1
    move2dir = {
        ">": 1,
        "^": -1j,
        "<": -1,
        "v": 1j,
    }
    for move in moves.replace("\n", ""):
        dir = move2dir[move]
        if pos + dir in wall:
            continue
        if pos + dir not in boxes:
            pos += dir
            continue
        boxes_to_move = 0
        pos_to_check = pos + dir
        while True:
            if pos_to_check in boxes:
                boxes_to_move += 1
                pos_to_check += dir
            elif pos_to_check in wall:
                boxes_to_move = 0
                break
            else:
                break
        if boxes_to_move > 0:
            pos += dir
            box_to_move = pos
            boxes.remove(pos)
            boxes.add(pos + boxes_to_move * dir)
    s = 0
    for box in boxes:
        s += box.real + 100 * box.imag
    return s

# Main execution function
def main():
    # Read the input from the file
    input_data = read_input('input15.txt')

    # Solve part a
    answer_a = a(input_data)
    print("Part A:", int(answer_a))

if __name__ == '__main__':
    main()