def read_input(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def find_regions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def dfs(x, y, plant_type):
        stack = [(x, y)]
        area, perimeter = 0, 0
        seen_edges = set()

        while stack:
            cx, cy = stack.pop()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True
            area += 1
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if not in_bounds(nx, ny) or grid[nx][ny] != plant_type:
                    perimeter += 1
                    seen_edges.add((cx, cy, nx, ny))
                elif not visited[nx][ny]:
                    stack.append((nx, ny))
        
        return area, perimeter

    total_cost = 0
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                area, perimeter = dfs(r, c, grid[r][c])
                total_cost += area * perimeter

    return total_cost

if __name__ == "__main__":
    grid = read_input("input12.txt")
    total_price = find_regions(grid)
    print("Total price:", total_price)
