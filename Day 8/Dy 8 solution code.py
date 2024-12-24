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
            for j in range(n):
                if i != j:
                    x1, y1 = positions[i]
                    x2, y2 = positions[j]

                    # Check if one is twice as far as the other
                    dx, dy = x2 - x1, y2 - y1
                    x3, y3 = x1 - dx, y1 - dy
                    x4, y4 = x2 + dx, y2 + dy

                    # Add valid antinodes to the set
                    if 0 <= x3 < len(map_data[0]) and 0 <= y3 < len(map_data):
                        antinodes.add((x3, y3))
                    if 0 <= x4 < len(map_data[0]) and 0 <= y4 < len(map_data):
                        antinodes.add((x4, y4))

    return antinodes

def main():
    map_data = read_map("input08.txt")
    antennas = find_antennas(map_data)
    antinodes = calculate_antinodes(map_data, antennas)
    print(f"Total unique antinode locations: {len(antinodes)}")

if __name__ == "__main__":
    main()
