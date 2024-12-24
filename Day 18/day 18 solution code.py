import heapq

def find_first_blocking_byte(input_file):
    # Read coordinates of falling bytes
    with open(input_file, 'r') as f:
        coordinates = [tuple(map(int, line.strip().split(','))) for line in f]

    # Define grid size and movement directions
    GRID_SIZE = 70
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Check if a path exists from start to goal
    def is_path_exists(corrupted):
        start = (0, 0)
        goal = (GRID_SIZE, GRID_SIZE)

        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            current = queue.pop(0)

            if current == goal:
                return True

            for dx, dy in DIRECTIONS:
                neighbor = (current[0] + dx, current[1] + dy)

                # Check if neighbor is valid (within grid and not corrupted)
                if (0 <= neighbor[0] <= GRID_SIZE and
                    0 <= neighbor[1] <= GRID_SIZE and
                    neighbor not in corrupted and
                    neighbor not in visited):
                    queue.append(neighbor)
                    visited.add(neighbor)

        return False

    # Track corrupted spaces and find first blocking byte
    corrupted = set()
    for i, coord in enumerate(coordinates):
        corrupted.add(coord)

        # Check if this coordinate blocks the path
        if not is_path_exists(corrupted):
            return coord

    return None  # No blocking byte found

# Read input from file and solve
result = find_first_blocking_byte('input18.txt')
print(f"First blocking byte coordinates: {result[0]},{result[1]}")
from collections import deque

def read_input(file_path):
    with open(file_path, "r") as file:
        return [tuple(map(int, line.strip().split(','))) for line in file]

def simulate_corruption(grid, corrupted_positions):
    for x, y in corrupted_positions:
        grid[y][x] = "#"

def bfs_shortest_path(grid, start, goal):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
    visited = set()
    visited.add(start)

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == goal:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 71 and 0 <= ny < 71 and (nx, ny) not in visited and grid[ny][nx] == ".":
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    return -1  # If no path exists

def main():
    # Initialize the grid
    grid_size = 71
    grid = [["."] * grid_size for _ in range(grid_size)]

    # Read input and simulate falling bytes
    corrupted_positions = read_input("input18.txt")[:1024]
    simulate_corruption(grid, corrupted_positions)

    # Find shortest path
    start = (0, 0)
    goal = (70, 70)
    result = bfs_shortest_path(grid, start, goal)

    print("Minimum number of steps:", result)

if __name__ == "__main__":
    main()