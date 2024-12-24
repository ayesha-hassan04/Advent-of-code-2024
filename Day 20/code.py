from collections import deque

# Read input from a file
def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

# Find the shortest path from start 'S' to end 'E' without cheating
def bfs_shortest_path(map_data, start, end):
    rows, cols = len(map_data), len(map_data[0])
    queue = deque([(start, 0)])  # (current position, current distance)
    visited = set()
    
    while queue:
        (x, y), distance = queue.popleft()
        
        if (x, y) == end:
            return distance
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and map_data[nx][ny] != '#' and (nx, ny) not in visited:
                queue.append(((nx, ny), distance + 1))
                visited.add((nx, ny))
    
    return float('inf')  # If no path exists

# Find the minimum time using cheating paths
def min_cheating_time(map_data, start, end, cheat_limit):
    rows, cols = len(map_data), len(map_data)
    best_time = float('inf')
    
    for x in range(rows):
        for y in range(cols):
            if map_data[x][y] == 'S':
                start_pos = (x, y)
            elif map_data[x][y] == 'E':
                end_pos = (x, y)
    
    # BFS with cheating allowed
    queue = deque([(start_pos, 0, 0)])  # (current position, current time, number of cheats used)
    visited = set()
    
    while queue:
        (x, y), current_time, cheats_used = queue.popleft()
        
        if (x, y) == end_pos:
            best_time = min(best_time, current_time)
            continue
        
        if cheats_used >= cheat_limit:
            continue
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < rows and 0 <= ny < cols:
                if map_data[nx][ny] == '#':
                    if cheats_used < cheat_limit:
                        queue.append(((nx, ny), current_time + 2, cheats_used + 1))
                else:
                    if (nx, ny, cheats_used) not in visited:
                        queue.append(((nx, ny), current_time + 1, cheats_used))
                        visited.add((nx, ny, cheats_used))
    
    return best_time

# Main execution
if __name__ == "__main__":
    file_path = "input20.txt"
    lines = read_input(file_path)
    
    map_data = lines[0:-1]
    start, end = (0, 0), (0, 0)
    cheat_limit = 2  # Maximum number of times cheating can be used
    
    # Find the shortest path without cheating
    shortest_time_without_cheat = bfs_shortest_path(map_data, start, end)
    
    # Find the shortest path with cheating allowed
    best_cheating_time = min_cheating_time(map_data, start, end, cheat_limit)
    
    total_time_saved = shortest_time_without_cheat - best_cheating_time
    print("Total cheats that save at least 100 picoseconds:", total_time_saved)
