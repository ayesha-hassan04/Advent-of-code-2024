from collections import defaultdict

# Function to read input from a file
def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

# Function to check if a design can be formed using available patterns
def can_form_design(design, patterns):
    dp = [0] * (len(design) + 1)
    dp[0] = 1  # Base case, empty design can be formed
    
    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]
    
    return dp[-1] > 0

# Main execution
if __name__ == "__main__":
    # Read input from file
    file_path = "input19.txt"
    lines = read_input(file_path)
    
    towel_patterns = lines[0].split(', ')
    desired_designs = lines[2:]
    
    # Count how many designs are possible
    possible_designs_count = 0
    for design in desired_designs:
        if can_form_design(design, towel_patterns):
            possible_designs_count += 1
    
    print("Number of possible designs:", possible_designs_count)
