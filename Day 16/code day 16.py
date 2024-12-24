import heapq

def parse_input(file_path):
    with open(file_path, "r") as file:
        maze = [list(line.strip()) for line in file]
    start, end = None, None
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "S":
                start = (x, y)
            elif cell == "E":
                end = (x, y)
    return maze, start, end

def neighbors(x, y, direction, maze):
    directions = ['N', 'E', 'S', 'W']
    dx_dy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    idx = directions.index(direction)

    # Forward movement
    nx, ny = x + dx_dy[idx][1], y + dx_dy[idx][0]
    if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] != "#":
        yield nx, ny, direction, 1  # Cost 1 for moving forward

    # Rotations
    left_direction = directions[(idx - 1) % 4]
    right_direction = directions[(idx + 1) % 4]
    yield x, y, left_direction, 1000  # Cost 1000 for turning left
    yield x, y, right_direction, 1000  # Cost 1000 for turning right

def find_lowest_cost(maze, start, end):
    directions = ['N', 'E', 'S', 'W']
    queue = [(0, start[0], start[1], 'E')]  # Start facing East
    visited = set()

    while queue:
        cost, x, y, direction = heapq.heappop(queue)
        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        if (x, y) == end:
            return cost

        for nx, ny, ndir, ncost in neighbors(x, y, direction, maze):
            if (nx, ny, ndir) not in visited:
                heapq.heappush(queue, (cost + ncost, nx, ny, ndir))

    return float('inf')  # If no path found

# Main Program
file_path = "input16.txt"
maze, start, end = parse_input(file_path)
lowest_cost = find_lowest_cost(maze, start, end)
print(f"The lowest score a Reindeer could possibly get is: {lowest_cost}")
