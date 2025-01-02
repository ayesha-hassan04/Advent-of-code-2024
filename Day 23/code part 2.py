#ead the input from the file
with open("input23.txt", "r") as file:
    connections = [line.strip() for line in file.readlines()]

# Parse connections into a graph representation
from collections import defaultdict

graph = defaultdict(set)
for connection in connections:
    a, b = connection.split('-')
    graph[a].add(b)
    graph[b].add(a)

# Find all sets of three inter-connected computers
triangles = set()
for node in graph:
    for neighbor1 in graph[node]:
        for neighbor2 in graph[node]:
            if neighbor1 != neighbor2 and neighbor2 in graph[neighbor1]:
                triangle = tuple(sorted([node, neighbor1, neighbor2]))
                triangles.add(triangle)

# Filter triangles where at least one name starts with "t"
filtered_triangles = [t for t in triangles if any(name.startswith('t') for name in t)]

# Output the result
print(f"Total triangles with at least one computer starting with 't': {len(filtered_triangles)}")

from collections import defaultdict

def read_input(file_name):
    """Reads input from the specified file."""
    with open(file_name, 'r') as file:
        connections = [line.strip().split('-') for line in file]
    return connections

def bron_kerbosch(graph, r, p, x, cliques):
    """Bron-Kerbosch algorithm to find maximal cliques."""
    if not p and not x:
        cliques.append(r)
        return
    for v in list(p):
        bron_kerbosch(
            graph,
            r.union({v}),
            p.intersection(graph[v]),
            x.intersection(graph[v]),
            cliques
        )
        p.remove(v)
        x.add(v)

def find_maximal_cliques(graph):
    """Finds all maximal cliques in the graph."""
    cliques = []
    bron_kerbosch(graph, set(), set(graph.keys()), set(), cliques)
    return cliques

def find_largest_clique(cliques):
    """Finds the largest clique among all cliques."""
    return max(cliques, key=len)

def generate_password(clique):
    """Generates the password from the largest clique."""
    return ",".join(sorted(clique))

def main():
    # Input file name
    input_file = "input23.txt"

    # Read input connections
    connections = read_input(input_file)

    # Build the adjacency list
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)

    # Find all maximal cliques
    cliques = find_maximal_cliques(graph)

    # Find the largest clique
    largest_clique = find_largest_clique(cliques)

    # Generate the password
    password = generate_password(largest_clique)
    print(f"Password to the LAN party: {password}")

if __name__ == "__main__":
    main()