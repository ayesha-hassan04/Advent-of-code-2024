from collections import deque

def parse_map(file_path):
    """Parse the topographic map from the input file."""
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def find_trailheads(height_map):
    """Find all trailhead positions (height 0) in the height map."""
    trailheads = []
    for row in range(len(height_map)):
        for col in range(len(height_map[0])):
            if height_map[row][col] == 0:
                trailheads.append((row, col))
    return trailheads

def find_distinct_trails(height_map, start):
    """
    Find all distinct hiking trails starting from a given trailhead.

    Args:
        height_map (list of list of int): The topographic map.
        start (tuple): The (row, col) of the trailhead.

    Returns:
        int: The number of distinct hiking trails starting from this trailhead.
    """
    rows, cols = len(height_map), len(height_map[0])
    queue = deque([(start, [start])])
    visited_trails = set()

    while queue:
        (current, path) = queue.popleft()
        row, col = current

        if height_map[row][col] == 9:
            visited_trails.add(tuple(path))
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) not in path and height_map[nr][nc] == height_map[row][col] + 1:
                    queue.append(((nr, nc), path + [(nr, nc)]))

    return len(visited_trails)

def calculate_total_rating(height_map):
    """Calculate the sum of the ratings of all trailheads."""
    trailheads = find_trailheads(height_map)
    total_rating = 0

    for trailhead in trailheads:
        total_rating += find_distinct_trails(height_map, trailhead)

    return total_rating

def main():
    # Read the input from the file "input10.txt"
    height_map = parse_map("input10.txt")

    # Calculate the total rating of all trailheads
    total_rating = calculate_total_rating(height_map)

    print("Total rating of all trailheads:", total_rating)

if __name__ == "__main__":
    main()
