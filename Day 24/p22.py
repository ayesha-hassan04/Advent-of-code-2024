from itertools import combinations
from collections import defaultdict, deque

def read_input(filename):
    with open(filename, "r") as f:
        sections = f.read().split("\n\n")
        initial_values = {}
        gates = {}
        for line in sections[0].strip().split("\n"):
            wire, value = line.split(": ")
            initial_values[wire] = int(value)

        for line in sections[1].strip().split("\n"):
            inputs, output = line.split(" -> ")
            wire_a, operator, wire_b = inputs.split()
            gates[output] = (wire_a, operator, wire_b)
        
    return initial_values, gates

def evaluate_circuit(initial_values, gates):
    # Initialize wire values with initial values
    wire_values = initial_values.copy()

    # Simulate the circuit
    while len(wire_values) < len(initial_values) + len(gates):
        for output, (wire_a, operator, wire_b) in gates.items():
            if output in wire_values:
                continue
            if wire_a in wire_values and wire_b in wire_values:
                val_a, val_b = wire_values[wire_a], wire_values[wire_b]
                if operator == "AND":
                    wire_values[output] = val_a & val_b
                elif operator == "OR":
                    wire_values[output] = val_a | val_b
                elif operator == "XOR":
                    wire_values[output] = val_a ^ val_b

    return wire_values

def part1(filename):
    initial_values, gates = read_input(filename)
    wire_values = evaluate_circuit(initial_values, gates)

    # Combine bits from wires starting with 'z'
    z_wires = sorted([wire for wire in wire_values if wire.startswith("z")])
    z_binary = "".join(str(wire_values[wire]) for wire in z_wires)
    z_decimal = int(z_binary, 2)

    return z_decimal

def find_swapped_gates(initial_values, gates):
    def test_system(swapped_gates):
        """Tests if the gates perform addition correctly."""
        for a in range(1 << len(x_wires)):
            for b in range(1 << len(y_wires)):
                # Set x and y values
                x_values = {x_wires[i]: (a >> i) & 1 for i in range(len(x_wires))}
                y_values = {y_wires[i]: (b >> i) & 1 for i in range(len(y_wires))}
                all_values = {**initial_values, **x_values, **y_values}

                # Simulate circuit
                result = evaluate_circuit(all_values, swapped_gates)

                # Check if z_wires represent (a + b)
                expected_sum = a + b
                z_binary = "".join(str(result[wire]) for wire in z_wires)
                if int(z_binary, 2) != expected_sum:
                    return False
        return True

    # Identify x, y, z wires
    x_wires = sorted(wire for wire in initial_values if wire.startswith("x"))
    y_wires = sorted(wire for wire in initial_values if wire.startswith("y"))
    z_wires = sorted(wire for wire in gates if wire.startswith("z"))

    # Generate all combinations of 4 pairs of swaps
    output_wires = list(gates.keys())
    for swaps in combinations(output_wires, 8):
        swapped_gates = gates.copy()

        # Apply swaps
        for i in range(0, len(swaps), 2):
            a, b = swaps[i], swaps[i + 1]
            swapped_gates[a], swapped_gates[b] = swapped_gates[b], swapped_gates[a]

        # Test the swapped gates
        if test_system(swapped_gates):
            return ",".join(sorted(swaps))

    return None


def part2(filename):
    initial_values, gates = read_input(filename)
    return find_swapped_gates(initial_values, gates)

# Solve both parts
filename = "input24.txt"
print("Part 1:", part1(filename))
print("Part 2:", part2(filename))
