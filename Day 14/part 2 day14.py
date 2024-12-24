import numpy as np
from typing import List, Tuple
import threading

class TimeoutException(Exception):
    pass

def timeout_handler():
    raise TimeoutException("Timeout reached while searching for Christmas tree pattern")

def parse_input(filename: str) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Parse input file to extract robot positions and velocities.

    Args:
        filename (str): Path to input file

    Returns:
        List of tuples, each containing (position, velocity)
    """
    robots = []
    with open(filename, 'r') as f:
        for line in f:
            try:
                pos_str, vel_str = line.strip().split(' ')
                px, py = map(int, pos_str[2:].strip('<>').split(','))
                vx, vy = map(int, vel_str[2:].strip('<>').split(','))
                robots.append(((px, py), (vx, vy)))
            except ValueError:
                print(f"Skipping invalid line: {line.strip()}")
    return robots

def simulate_robots(robots: List[Tuple[Tuple[int, int], Tuple[int, int]]],
                    time: int,
                    width: int,
                    height: int) -> np.ndarray:
    """
    Simulate robot movements and count robot positions after given time.

    Args:
        robots (List): List of robot (position, velocity) tuples
        time (int): Seconds to simulate
        width (int): Space width
        height (int): Space height

    Returns:
        numpy array of robot count per tile
    """
    grid = np.zeros((height, width), dtype=int)

    for (px, py), (vx, vy) in robots:
        final_x = (px + vx * time) % width
        final_y = (py + vy * time) % height
        grid[final_y, final_x] += 1

    return grid

def is_christmas_tree(grid: np.ndarray) -> bool:
    """
    Check if the robot positions form a Christmas tree pattern.

    Args:
        grid (numpy array): Robot position grid

    Returns:
        Boolean indicating if a Christmas tree pattern is found
    """
    tree_pattern = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
    ]

    height, width = grid.shape
    pattern_height, pattern_width = len(tree_pattern), len(tree_pattern[0])

    for y in range(height - pattern_height + 1):
        for x in range(width - pattern_width + 1):
            match = True
            for dy in range(pattern_height):
                for dx in range(pattern_width):
                    if tree_pattern[dy][dx] == 1 and grid[y + dy, x + dx] == 0:
                        match = False
                        break
                if not match:
                    break

            if match:
                return True

    return False

def find_christmas_tree_time(filename: str, max_time: int = 10000, width: int = 101, height: int = 103) -> int:
    """
    Find the earliest time when robots form a Christmas tree pattern.

    Args:
        filename (str): Input file path
        max_time (int): Maximum time to search
        width (int): Space width
        height (int): Space height

    Returns:
        Time when Christmas tree pattern is found, or -1 if not found
    """
    robots = parse_input(filename)
    timeout = threading.Timer(10, timeout_handler)  # 10-second timeout

    try:
        timeout.start()
        for time in range(max_time):
            grid = simulate_robots(robots, time, width, height)

            if is_christmas_tree(grid):
                return time
    except TimeoutException:
        print("Timeout reached while searching for Christmas tree pattern.")
        return -1
    finally:
        timeout.cancel()

    return -1

# Solve the problem
if __name__ == "__main__":
    result = find_christmas_tree_time('input14.txt')
    if result != -1:
        print(f"Seconds until Christmas Tree Pattern: {result}")
    else:
        print("Christmas tree pattern not found within the given time limit.")