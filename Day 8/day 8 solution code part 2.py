import math

def read_map(file_path):
    """Reads the map from the input file and returns it as a list of strings."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def find_antennas(map_data):
    """Finds all antennas in the map and their positions."""
    antennas = {}
    for y, row in enumerate(map_data):
        for x, char in enumerate(row):
            if char.isalnum():  # Antennas are letters or digits
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas

def calculate_antinodes(map_data, antennas):
    """Calculates all unique antinode positions in the map."""
    antinodes = set()

    for frequency, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            antinodes.add(positions[i])  # Each antenna itself is an antinode
            for j in range(n):
                if i != j:
                    x1, y1 = positions[i]
                    x2, y2 = positions[j]

                    # Calculate all points between and beyond the two antennas
                    dx, dy = x2 - x1, y2 - y1
                    gcd = abs(dx) if dy == 0 else abs(dy) if dx == 0 else abs(math.gcd(dx, dy))
                    dx //= gcd
                    dy //= gcd

                    # Extend in both directions
                    x, y = x1, y1
                    while 0 <= x < len(map_data[0]) and 0 <= y < len(map_data):
                        antinodes.add((x, y))
                        x -= dx
                        y -= dy

                    x, y = x1 + dx, y1 + dy
                    while 0 <= x < len(map_data[0]) and 0 <= y < len(map_data):
                        antinodes.add((x, y))
                        x += dx
                        y += dy

    return antinodes

def main():
    map_data = read_map("input08.txt")
    antennas = find_antennas(map_data)
    antinodes = calculate_antinodes(map_data, antennas)
    print(f"Total unique antinode locations: {len(antinodes)}")

if __name__ == "__main__":
    main()
