from graph import Graph
import json
import io

graph_data = {
    1: {2, 9},
    2: {3, 5, 1},
    3: {4, 2},
    4: {3},
    5: {2, 6},
    6: {5, 7},
    7: {6, 8, 10},
    8: {7},
    9: {1, 10},
    10: {9, 7, 11},
    11: {10}
}

G = Graph()
value = 1 #Weight on each edge (for now lets just put 1)

for node, neighbours in graph_data.items():
    G.add_node(node)
    for neighbour in neighbours:
        G.add_node(neighbour)
        G.add_edge(node, neighbour, value)

node1 = G.get_node(5)
node2 = G.get_node(4)
print(node1.neighbors)
print(node1.neighbors)

tsp_size = len(city_names)
num_routes = 1
depot = 0

