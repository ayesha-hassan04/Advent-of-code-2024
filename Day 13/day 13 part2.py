def read_input(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

def min_tokens_to_win(prizes):
    min_tokens = float('inf')

    for prize in prizes:
        a_part, b_part, p_part = prize.split(' ')
        
        # Parse A and B moves
        a_x, a_y = map(int, a_part.split('+'))
        b_x, b_y = map(int, b_part.split('+'))
        
        # Parse prize position
        p_x, p_y = map(int, p_part.split('=')[1].split(','))
        
        # Apply the large offset to the prize position
        p_x += 10**13
        p_y += 10**13
        
        # Calculate A and B presses
        a_presses = p_x // a_x
        b_presses = p_y // b_y
        cost = a_presses * 3 + b_presses * 1
        
        # Check if more presses are needed
        if p_x != a_presses * a_x or p_y != b_presses * b_y:
            a_presses += 1
            b_presses += 1
            cost = a_presses * 3 + b_presses * 1
        
        min_tokens = min(min_tokens, cost)
    
    return min_tokens

if __name__ == "__main__":
    prizes = read_input("input13.txt")
    min_cost = min_tokens_to_win(prizes)
    print("Minimum tokens required:", min_cost)
