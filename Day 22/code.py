def generate_secret_number(secret, steps):
    """Generate the nth secret number given an initial secret and steps."""
    for _ in range(steps):
        # Step 1: Multiply by 64, mix, and prune
        secret ^= (secret * 64) % 16777216
        # Step 2: Divide by 32 (rounded down), mix, and prune
        secret ^= (secret // 32) % 16777216
        # Step 3: Multiply by 2048, mix, and prune
        secret ^= (secret * 2048) % 16777216
        secret %= 16777216
    return secret

def calculate_total(input_file):
    """Calculate the sum of the 2000th secret number for each buyer."""
    with open(input_file, 'r') as file:
        initial_secrets = [int(line.strip()) for line in file.readlines()]

    total = 0
    for secret in initial_secrets:
        total += generate_secret_number(secret, 2000)

    return total

def main():
    input_file = "input22.txt"
    total = calculate_total(input_file)
    print("Sum of 2000th secret numbers:", total)

if __name__ == "__main__":
    main()
