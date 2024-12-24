def evolve_stones(stones, blinks):
    """
    Simulates the evolution of stones over a specified number of blinks.

    Args:
        stones (list of int): The initial list of stones.
        blinks (int): Number of blinks to simulate.

    Returns:
        int: The number of stones after the specified number of blinks.
    """
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                new_stones.extend([left, right])
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)

def main():
    # Read the input from the file "input11.txt"
    with open("input11.txt", "r") as file:
        puzzle_input = file.read().strip()

    # Parse the input into a list of integers.
    stones = list(map(int, puzzle_input.split()))

    # Number of blinks to simulate.
    blinks = 25

    # Simulate the evolution of stones and print the result.
    result = evolve_stones(stones, blinks)
    print("Number of stones after 25 blinks:", result)

if __name__ == "__main__":
    main()
