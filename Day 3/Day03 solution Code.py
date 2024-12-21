import re

def sum_valid_mul_with_conditions(file):
    with open("input03.txt", "r") as f:
        data = f.read()

    # Regular expressions for instructions
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # Initialize variables
    enabled = True  # At the start, mul instructions are enabled
    total_sum = 0

    # Iterate through instructions in order
    instructions = re.finditer(fr"{mul_pattern}|{do_pattern}|{dont_pattern}", data)
    for match in instructions:
        if match.group(0).startswith("mul"):
            # Process mul instruction if enabled
            if enabled:
                x, y = map(int, match.groups())
                total_sum += x * y
        elif match.group(0) == "do()":
            # Enable mul instructions
            enabled = True
        elif match.group(0) == "don't()":
            # Disable mul instructions
            enabled = False

    return total_sum

# Run the function with the input file
file_name = "input03.txt"
result = sum_valid_mul_with_conditions("input03.txt")
print(f"The total sum of valid enabled mul results is: {result}")
