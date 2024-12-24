def parse_topographic_map(filename):
    """
    Reads the topographic map from the file and returns it as a 2D list of integers.

    Args:
        filename (str): The name of the file containing the topographic map.

    Returns:
        list[list[int]]: The topographic map.
    """
    with open(filename, "r") as file:
        return [list(map(int, line.strip())) for line in file]

def find_trailheads(topographic_map):
    """
    Find all trailheads (positions with height 0) in the topographic map.

    Args:
        topographic_map (list[list[int]]): The topographic map.

    Returns:
        list[tuple[int, int]]: The list of trailhead coordinates.
    """
    trailheads = []
    for row in range(len(topographic_map)):
        for col in range(len(topographic_map[row])):
            if topographic_map[row][col] == 0:
                trailheads.append((row, col))
    return trailheads

def dfs(topographic_map, row, col, visited):
    """
    Perform a depth-first search to find all reachable 9s from a given position.

    Args:
        topographic_map (list[list[int]]): The topographic map.
        row (int): The current row position.
        col (int): The current column position.
        visited (set): The set of visited coordinates.

    Returns:
        int: The number of 9s reachable from the given position.
    """
    stack = [(row, col)]
    reachable_nines = 0
    while stack:
        current_row, current_col = stack.pop()
        if (current_row, current_col) in visited:
            continue
        visited.add((current_row, current_col))

        # Check if we reached a 9
        if topographic_map[current_row][current_col] == 9:
            reachable_nines += 1

        # Explore neighbors (up, down, left, right)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current_row + dr, current_col + dc
            if (
                0 <= nr < len(topographic_map)
                and 0 <= nc < len(topographic_map[0])
                and (nr, nc) not in visited
                and topographic_map[nr][nc] == topographic_map[current_row][current_col] + 1
            ):
                stack.append((nr, nc))

    return reachable_nines

def calculate_trailhead_scores(topographic_map):
    """
    Calculate the score for all trailheads in the topographic map.

    Args:
        topographic_map (list[list[int]]): The topographic map.

    Returns:
        int: The sum of all trailhead scores.
    """
    trailheads = find_trailheads(topographic_map)
    total_score = 0
    for row, col in trailheads:
        visited = set()
        score = dfs(topographic_map, row, col, visited)
        total_score += score
    return total_score

def main():
    # Read the topographic map from "input10.txt"
    topographic_map = parse_topographic_map("input10.txt")

    # Calculate the total score of all trailheads
    total_score = calculate_trailhead_scores(topographic_map)

    print("Total Score of All Trailheads:", total_score)

if __name__ == "__main__":
    main()

