from itertools import product

def read_input(file_path):
    """Reads the input file and returns a list of equations."""
    equations = []
    with open(file_path, 'r') as file:
        for line in file:
            test_value, numbers = line.strip().split(":")
            test_value = int(test_value)
            numbers = list(map(int, numbers.split()))
            equations.append((test_value, numbers))
    return equations

def evaluate_expression(numbers, operators):
    """Evaluates the expression formed by numbers and operators left-to-right."""
    result = numbers[0]
    for num, op in zip(numbers[1:], operators):
        if op == '+':
            result += num
        elif op == '*':
            result *= num
        elif op == '||':
            result = int(f"{result}{num}")
    return result

def is_valid_equation(test_value, numbers):
    """Checks if any operator combination can produce the test value."""
    num_count = len(numbers)
    operator_combinations = product(['+', '*', '||'], repeat=num_count - 1)
    for operators in operator_combinations:
        if evaluate_expression(numbers, operators) == test_value:
            return True
    return False

def calculate_total_calibration(equations):
    """Calculates the total calibration result for valid equations."""
    total = 0
    for test_value, numbers in equations:
        if is_valid_equation(test_value, numbers):
            total += test_value
    return total

def main():
    equations = read_input("input07.txt")
    total = calculate_total_calibration(equations)
    print(f"Total calibration result: {total}")

if __name__ == "__main__":
    main()
