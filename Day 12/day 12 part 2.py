def read_map(file_path):
    """Reads the garden map from the input file."""
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def flood_fill(grid, x, y, visited, plant_type):
    """Performs flood-fill to find a region and calculates its area and perimeter."""
    rows, cols = len(grid), len(grid[0])
    stack = [(x, y)]
    area = 0
    perimeter = 0
    visited.add((x, y))

    # Directions for movement: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        cx, cy = stack.pop()
        area += 1

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == plant_type:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        stack.append((nx, ny))
                else:
                    # Edge of the region
                    perimeter += 1
            else:
                # Edge of the grid
                perimeter += 1

    return area, perimeter

def calculate_fencing_cost(grid):
    """Calculates the total fencing cost for the garden."""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    total_cost = 0

    for x in range(rows):
        for y in range(cols):
            if (x, y) not in visited:
                # Start a new region
                plant_type = grid[x][y]
                area, perimeter = flood_fill(grid, x, y, visited, plant_type)
                total_cost += area * perimeter

    return total_cost

def main():
    # Read the garden map from the input file
    file_path = "input12.txt"
    garden_map = read_map(file_path)

    # Calculate the total fencing cost
    total_cost = calculate_fencing_cost(garden_map)

    # Output the result
    print("Total fencing cost:", total_cost)

if __name__ == "__main__":
    main()

     

import numpy as np

# Define the ORTHOGONAL_DIRS variable
ORTHOGONAL_DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get(lines, pos, default):
    """
    Helper function to safely access the value at position `pos` in the `lines` list.
    If the position is out of bounds, return the `default` value.
    """
    x, y = pos
    if 0 <= x < len(lines) and 0 <= y < len(lines[0]):
        return lines[x][y]
    return default

def calculate_total_area_and_perimeter(input_file):
    # Read the input file
    with open(input_file, 'r') as f:
        lines = [list(line.strip()) for line in f.readlines()]

    total = 0
    visited = set()

    for i, row in enumerate(lines):
        for j, c in enumerate(row):
            if (i, j) in visited:
                continue

            visited_perimeter = set()
            stack = [(i, j)]
            area = 0
            perimeter = 0

            while stack:
                x, y = stack.pop()
                if (x, y) in visited:
                    continue

                for d in ORTHOGONAL_DIRS:
                    if get(lines, (x + d[0], y + d[1]), None) == c:
                        stack.append((x + d[0], y + d[1]))
                    else:
                        if ((x, y), (x + d[0], y + d[1])) in visited_perimeter:
                            continue

                        perimeter += 1
                        visited_perimeter.add(((x, y), (x + d[0], y + d[1])))

                        curr = (x, y)
                        ortho = np.array([[0, 1], [-1, 0]]) @ np.array(d)

                        while True:
                            curr = ortho + curr
                            if get(lines, tuple(curr), None) == c and get(lines, tuple(np.array(d) + curr), None) != c:
                                visited_perimeter.add((tuple(curr), tuple(np.array(d) + curr)))
                            else:
                                break

                        curr = (x, y)
                        ortho = np.array([[0, -1], [1, 0]]) @ np.array(d)

                        while True:
                            curr = ortho + curr
                            if get(lines, tuple(curr), None) == c and get(lines, tuple(np.array(d) + curr), None) != c:
                                visited_perimeter.add((tuple(curr), tuple(np.array(d) + curr)))
                            else:
                                break

                area += 1
                visited.add((x, y))

            total += area * perimeter

    return total

# Example usage:
input_file = 'input.txt'  # Specify the path to your input file
total = calculate_total_area_and_perimeter(input_file)
print(total)