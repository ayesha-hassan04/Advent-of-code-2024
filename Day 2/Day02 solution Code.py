def is_safe(report):
    # Check if the report is either all increasing or all decreasing
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def can_be_safe_with_removal(report):
    # Try removing each level and check if the remaining report is safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Remove the i-th level
        if is_safe(modified_report):
            return True
    return False

def count_safe_reports_with_dampener(file):
    with open("input02.txt", "r") as f:
        reports = [list(map(int, line.split())) for line in f]

    # Count reports that are safe or can be made safe by removing one level
    safe_count = 0
    for report in reports:
        if is_safe(report) or can_be_safe_with_removal(report):
            safe_count += 1
    return safe_count

# Run the function with the given input file
file_name = "input02.txt"
safe_count = count_safe_reports_with_dampener("input02.txt")
print(f"Number of Safe Reports (with Dampener): {safe_count}")
