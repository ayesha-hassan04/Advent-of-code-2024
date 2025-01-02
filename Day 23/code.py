from collections import defaultdict
from itertools import combinations

def read_input(file_path):
    """Read the input file and parse the connections."""
    connections = []
    with open(file_path, 'r') as file:
        for line in file:
            connections.append(tuple(line.strip().split('-')))
    return connections

def build_graph(connections):
    """Build an undirected graph from the list of connections."""
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)
    return graph

def find_triangles(graph):
    """Find all sets of three inter-connected computers in the graph."""
    triangles = set()
    for node in graph:
        neighbors = graph[node]
        for a, b in combinations(neighbors, 2):
            if a in graph[b]:
                triangle = tuple(sorted([node, a, b]))
                triangles.add(triangle)
    return triangles

def count_t_triangles(triangles):
    """Count triangles containing at least one name starting with 't'."""
    return sum(1 for triangle in triangles if any(computer.startswith('t') for computer in triangle))

def main():
    input_file = "input23.txt"
    connections = read_input(input_file)
    graph = build_graph(connections)
    triangles = find_triangles(graph)
    result = count_t_triangles(triangles)
    print("Number of triangles with at least one 't' computer:", result)

if __name__ == "__main__":
    main()
