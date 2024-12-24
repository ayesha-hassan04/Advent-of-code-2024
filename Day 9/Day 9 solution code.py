def parse_disk_map(disk_map):
    """
    Parse the disk map into a list of file and free space segments.
    
    Args:
        disk_map (str): The disk map string.

    Returns:
        list of tuples: A list where each tuple contains the length of a file or free space segment
                        and a boolean indicating if it is a file (True for file, False for free space).
    """
    segments = []
    for i in range(len(disk_map)):
        length = int(disk_map[i])
        is_file = (i % 2 == 0)
        segments.append((length, is_file))
    return segments

def generate_initial_layout(segments):
    """
    Generate the initial disk layout as a string representation.

    Args:
        segments (list of tuples): The parsed disk segments.

    Returns:
        str: The initial layout of the disk.
    """
    layout = []
    file_id = 0
    for length, is_file in segments:
        if is_file:
            layout.extend([str(file_id)] * length)
            file_id += 1
        else:
            layout.extend(['.'] * length)
    return ''.join(layout)

def compact_disk(layout):
    """
    Compact the disk layout by moving file blocks to the leftmost free spaces.

    Args:
        layout (str): The current disk layout.

    Returns:
        str: The compacted disk layout.
    """
    layout = list(layout)
    left = 0
    for right in range(len(layout)):
        if layout[right] != '.':
            while layout[left] != '.' and left < right:
                left += 1
            if left < right:
                layout[left], layout[right] = layout[right], '.'
                left += 1
    return ''.join(layout)

def calculate_checksum(layout):
    """
    Calculate the checksum of the disk layout.

    Args:
        layout (str): The compacted disk layout.

    Returns:
        int: The checksum of the layout.
    """
    checksum = 0
    for position, block in enumerate(layout):
        if block != '.':
            checksum += position * int(block)
    return checksum

def main():
    # Read the input from the file "input09.txt"
    with open("input09.txt", "r") as file:
        puzzle_input = file.read().strip()

    # Parse the input and generate the initial layout.
    segments = parse_disk_map(puzzle_input)
    initial_layout = generate_initial_layout(segments)

    # Compact the disk and calculate the checksum.
    compacted_layout = compact_disk(initial_layout)
    checksum = calculate_checksum(compacted_layout)

    print("Initial layout:", initial_layout)
    print("Compacted layout:", compacted_layout)
    print("Checksum:", checksum)

if __name__ == "__main__":
    main()
