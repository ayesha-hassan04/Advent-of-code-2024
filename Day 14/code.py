def read_input(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def parse_robot(line):
    position, velocity = line.split(' ')
    p_x, p_y = map(int, position[2:].split(','))
    v_x, v_y = map(int, velocity[2:].split(','))
    return (p_x, p_y, v_x, v_y)

def simulate_robots(robots, width, height, time):
    positions = []
    for p_x, p_y, v_x, v_y in robots:
        new_x = (p_x + v_x * time) % width
        new_y = (p_y + v_y * time) % height
        positions.append((new_x, new_y))
    return positions

def count_quadrants(positions, width, height):
    mid_x, mid_y = width // 2, height // 2
    quadrants = [0, 0, 0, 0]  # Top-left, Top-right, Bottom-left, Bottom-right

    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue  # Skip robots on the middle lines
        if x < mid_x and y < mid_y:
            quadrants[0] += 1  # Top-left
        elif x >= mid_x and y < mid_y:
            quadrants[1] += 1  # Top-right
        elif x < mid_x and y >= mid_y:
            quadrants[2] += 1  # Bottom-left
        elif x >= mid_x and y >= mid_y:
            quadrants[3] += 1  # Bottom-right

    return quadrants

if __name__ == "__main__":
    # Parameters
    width, height = 101, 103
    time = 100

    # Read and parse input
    data = read_input("input14.txt")
    robots = [parse_robot(line) for line in data]

    # Simulate robot movements
    positions = simulate_robots(robots, width, height, time)

    # Count robots in each quadrant
    quadrants = count_quadrants(positions, width, height)

    # Calculate safety factor
    safety_factor = 1
    for count in quadrants:
        safety_factor *= count

    print("Quadrants:", quadrants)
    print("Safety Factor:", safety_factor)
