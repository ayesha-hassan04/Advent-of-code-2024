from collections import Counter

def evolve_stones_efficiently(stones, blinks):
    """
    Simulates the evolution of stones over a specified number of blinks efficiently.

    Args:
        stones (list of int): The initial list of stones.
        blinks (int): Number of blinks to simulate.

    Returns:
        int: The number of stones after the specified number of blinks.
    """
    # Use a Counter to track counts of each stone.
    stone_counts = Counter(stones)

    for _ in range(blinks):
        new_stone_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                new_stone_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                new_stone_counts[left] += count
                new_stone_counts[right] += count
            else:
                new_stone_counts[stone * 2024] += count
        stone_counts = new_stone_counts

    # Sum the counts of all stones.
    return sum(stone_counts.values())

def main():
    # Read the input from the file "input11.txt"
    with open("input11.txt", "r") as file:
        puzzle_input = file.read().strip()

    # Parse the input into a list of integers.
    stones = list(map(int, puzzle_input.split()))

    # Number of blinks to simulate.
    blinks = 75

    # Simulate the evolution of stones and print the result.
    result = evolve_stones_efficiently(stones, blinks)
    print("Number of stones after 75 blinks:", result)

if __name__ == "__main__":
    main()
