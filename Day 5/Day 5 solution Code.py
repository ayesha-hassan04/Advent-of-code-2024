def parse_input(filename):
    with open(filename, 'r') as file:
        data = file.read().strip().split('\n\n')

    rules = data[0].split('\n')
    updates = data[1].split('\n')

    parsed_rules = []
    for rule in rules:
        x, y = map(int, rule.split('|'))
        parsed_rules.append((x, y))

    parsed_updates = []
    for update in updates:
        pages = list(map(int, update.split(',')))
        parsed_updates.append(pages)

    return parsed_rules, parsed_updates

def is_update_in_order(update, rules):
    # Create a map of page positions for quick lookup
    position = {page: idx for idx, page in enumerate(update)}

    for x, y in rules:
        if x in position and y in position:  # Only check rules involving pages in the update
            if position[x] > position[y]:
                return False

    return True

def find_middle_page(update):
    mid_index = len(update) // 2
    return update[mid_index]

def process_updates(filename):
    rules, updates = parse_input(filename)
    total = 0

    for update in updates:
        if is_update_in_order(update, rules):
            total += find_middle_page(update)

    return total

# Run the solution
file_name = "input05.txt"
result = process_updates(file_name)
print("The sum of the middle page numbers from correctly-ordered updates is:", result)
