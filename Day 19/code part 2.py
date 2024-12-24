from collections import defaultdict

# Function to read input from a file
def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

# Function to count all combinations to form the design
def count_ways(design, patterns, memo):
    if design in memo:
        return memo[design]
    
    if not design:
        return 1  # An empty design can always be formed

    total_ways = 0
    for pattern in patterns:
        if design.startswith(pattern):
            total_ways += count_ways(design[len(pattern):], patterns, memo)
    
    memo[design] = total_ways
    return total_ways

# Main execution
if __name__ == "__main__":
    file_path = "input19.txt"
    lines = read_input(file_path)
    
    towel_patterns = lines[0].split(', ')
    desired_designs = lines[2:]
    
    memo = {}  # Cache to store the results of subproblems
    total_ways = 0
    
    for design in desired_designs:
        total_ways += count_ways(design, towel_patterns, memo)
    
    print("Total number of ways:", total_ways)
