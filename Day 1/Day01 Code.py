from collections import Counter
#part 1
def calculate_similarity_score(file):
    # Read the file and split into left and right lists
    with open("input.txt", "r") as file:
        left_list = []
        right_list = []
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    # Count occurrences in the right list
    right_count = Counter(right_list)

    # Calculate the similarity score
    similarity_score = 0
    for number in left_list:
        similarity_score += number * right_count.get(number, 0)

    return similarity_score

# Run the function with the given input file
file_name = "input.txt"
similarity_score = calculate_similarity_score(file_name)
print(f"Similarity Score: {similarity_score}")
