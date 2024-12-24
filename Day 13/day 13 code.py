def solve_machine(machine):
    """Find the minimum token solution for a machine."""
    ax, ay = machine['A']
    bx, by = machine['B']
    px, py = machine['prize']
    
    min_tokens = float('inf')
    best_solution = None
    
    # Brute force all possible combinations
    for a in range(101):  # 0 to 100 inclusive
        for b in range(101):  # 0 to 100 inclusive
            # Calculate positions
            x_pos = a * ax + b * bx
            y_pos = a * ay + b * by
            
            # Check if position matches exactly
            if x_pos == px and y_pos == py:
                tokens = (a * 3) + (b * 1)
                if tokens < min_tokens:
                    min_tokens = tokens
                    best_solution = (a, b, tokens)
    
    return best_solution

def read_input(filename):
    machines = []
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
        
    i = 0
    while i < len(lines):
        # Parse button A
        a_line = lines[i].replace("Button A: ", "")
        ax = int(a_line.split("X+")[1].split(",")[0])
        ay = int(a_line.split("Y+")[1])
        
        # Parse button B
        b_line = lines[i+1].replace("Button B: ", "")
        bx = int(b_line.split("X+")[1].split(",")[0])
        by = int(b_line.split("Y+")[1])
        
        # Parse prize
        p_line = lines[i+2].replace("Prize: ", "")
        px = int(p_line.split("X=")[1].split(",")[0])
        py = int(p_line.split("Y=")[1])
        
        machines.append({
            'A': (ax, ay),
            'B': (bx, by),
            'prize': (px, py)
        })
        
        i += 3
        
    return machines

def solve_claw_puzzle(filename):
    machines = read_input(filename)
    total_tokens = 0
    solutions = []
    
    print("\nDetailed solutions for each machine:")
    print("=" * 50)
    
    for i, machine in enumerate(machines, 1):
        print(f"\nMachine {i}:")
        print(f"Button A: X+{machine['A'][0]}, Y+{machine['A'][1]}")
        print(f"Button B: X+{machine['B'][0]}, Y+{machine['B'][1]}")
        print(f"Prize: X={machine['prize'][0]}, Y={machine['prize'][1]}")
        
        solution = solve_machine(machine)
        if solution:
            a_presses, b_presses, tokens = solution
            print("\nSolution found!")
            print(f"A presses: {a_presses} (cost: {a_presses * 3} tokens)")
            print(f"B presses: {b_presses} (cost: {b_presses * 1} tokens)")
            print(f"Total tokens: {tokens}")
            
            # Verify solution
            final_x = a_presses * machine['A'][0] + b_presses * machine['B'][0]
            final_y = a_presses * machine['A'][1] + b_presses * machine['B'][1]
            print(f"\nVerification:")
            print(f"X coordinate: {final_x} (target: {machine['prize'][0]})")
            print(f"Y coordinate: {final_y} (target: {machine['prize'][1]}")
            
            if final_x == machine['prize'][0] and final_y == machine['prize'][1]:
                print("✓ Solution verified!")
                total_tokens += tokens
                solutions.append((i, a_presses, b_presses, tokens))
            else:
                print("✗ Solution verification failed!")
        else:
            print("No valid solution found")
        
        print("=" * 50)
    
    print("\nSummary:")
    print(f"Solvable machines: {len(solutions)}")
    for i, a, b, tokens in solutions:
        print(f"Machine {i}: {a} A presses, {b} B presses, {tokens} tokens")
    print(f"Total tokens needed: {total_tokens}")
    
    return total_tokens

if __name__ == "__main__":
    result = solve_claw_puzzle("input13.txt")