from math import gcd


def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find gcd and coefficients."""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def solve_claw_machine(Ax, Ay, Bx, By, Px, Py):
    """Solve a single claw machine to find the fewest tokens."""
    # Adjust prize positions by 10^13
    Px += 10**13
    Py += 10**13

    # Check if it's possible to solve
    det = Ax * By - Ay * Bx
    if det == 0:
        return None  # Parallel or no solution

    # Use extended Euclidean algorithm to solve
    g, x, y = extended_gcd(det, By)
    if (Px * By - Py * Bx) % g != 0:
        return None  # No solution

    # Scale the solution
    scale = (Px * By - Py * Bx) // g
    a = x * scale
    b = y * scale

    # Minimize cost (3a + b)
    # Ensure valid integers for a and b
    if a < 0 or b < 0:
        return None

    cost = 3 * abs(a) + abs(b)
    return cost


def parse_line(line):
    """Parse a single line to extract integers."""
    line = line.split(": ")[1]
    return list(map(int, line.replace("X+", "").replace("Y+", "").split(", ")))


def solve_all(filename):
    """Solve all claw machines and find the fewest tokens for all prizes."""
    with open(filename, "r") as f:
        blocks = f.read().strip().split("\n\n")

    min_cost = 0
    prizes_won = 0
    for block in blocks:
        lines = block.strip().split("\n")
        Ax, Ay = parse_line(lines[0])
        Bx, By = parse_line(lines[1])
        Px, Py = map(int, lines[2].split(": ")[1].replace("X=", "").replace("Y=", "").split(", "))

        cost = solve_claw_machine(Ax, Ay, Bx, By, Px, Py)
        if cost is not None:
            min_cost += cost
            prizes_won += 1

    return prizes_won, min_cost


if __name__ == "__main__":
    filename = "input13.txt"
    prizes, fewest_tokens = solve_all(filename)
    print(f"Prizes Won: {prizes}")
    print(f"Fewest Tokens for Part Two: {fewest_tokens}")
