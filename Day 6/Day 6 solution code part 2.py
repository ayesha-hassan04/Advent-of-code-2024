def parse_input(file_name):
    with open(file_name, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return grid

def move_guard_with_obstruction(grid, obstruction):
    rows, cols = len(grid), len(grid[0])
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    direction_order = ['^', '>', 'v', '<']

    # Find the initial position and direction of the guard
    guard_pos = None
    guard_dir = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                guard_pos = (r, c)
                guard_dir = grid[r][c]
                break
        if guard_pos:
            break

    # Place the obstruction
    grid[obstruction[0]][obstruction[1]] = '#'

    visited = set()
    path = []  # To track path for detecting loops

    while True:
        r, c = guard_pos
        dr, dc = directions[guard_dir]
        next_r, next_c = r + dr, c + dc

        # If the guard can't move forward, turn right 90 degrees
        if not (0 <= next_r < rows and 0 <= next_c < cols) or grid[next_r][next_c] == '#':
            current_dir_idx = direction_order.index(guard_dir)
            guard_dir = direction_order[(current_dir_idx + 1) % 4]
        else:
            # Move forward
            guard_pos = (next_r, next_c)

        # Record the path
        path.append(guard_pos)
        if guard_pos in visited:
            break  # Loop detected
        visited.add(guard_pos)

        # Check if the guard has moved out of bounds
        if not (0 <= guard_pos[0] < rows and 0 <= guard_pos[1] < cols):
            break

    # Remove the obstruction for subsequent simulations
    grid[obstruction[0]][obstruction[1]] = '.'

    return len(path) != len(set(path))  # Returns True if a loop is detected

def find_loop_positions(file_name):
    grid = parse_input(file_name)
    rows, cols = len(grid), len(grid[0])
    valid_positions = 0

    # Guard's starting position
    start_pos = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in {'^', '>', 'v', '<'}:
                start_pos = (r, c)
                break
        if start_pos:
            break

    # Try placing an obstruction at every valid position
    for r in range(rows):
        for c in range(cols):
            if (r, c) != start_pos and grid[r][c] == '.':  # Skip starting position and existing obstructions
                if move_guard_with_obstruction([row[:] for row in grid], (r, c)):
                    valid_positions += 1

    return valid_positions

# Main execution
file_name = "input06.txt"
result = find_loop_positions(file_name)
print("Number of positions where an obstruction would cause a loop:", result)
