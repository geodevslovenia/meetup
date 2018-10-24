from edge import Edge
from node import Node


class Graph:

    def __init__(self, nodes=None, edges=None):
        if edges is None:
            edges = {}
        if nodes is None:
            nodes = {}
        self.nodes = nodes
        self.edges = edges

    def get_edges(self):
        return self.edges

    def get_nodes(self):
        return self.nodes

    def get_nodes_count(self):
        return len(self.nodes)

    def get_edges_count(self):
        return len(self.edges)

    def add_node(self, node_id):
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id)

    def get_node(self, node_id):
        return self.nodes[node_id]

    def get_edge(self, node_1, node_2, directed=False):
        if node_1 not in self.nodes or node_2 not in self.nodes:
            print('One of the nodes does not exists')
            return
        key_1 = self.get_edge_key(node_1, node_2)

        if key_1 in self.edges:
            return self.edges[key_1]

        if not directed:
            key_2 = self.get_edge_key(node_2, node_1)
            if key_2 in self.edges:
                return self.edges[key_2]

    def add_edge(self, node_1, node_2, value=1):
        if node_1 == node_2:
            print('Same ', node_1, node_2)
            return

        if node_1 not in self.nodes or node_2 not in self.nodes:
            print('Node does not exists in graph')
            return

        key = self.get_edge_key(node_1, node_2)
        if key not in self.edges:
            self.edges[key] = Edge(node_1, node_2, value)
            self.nodes[node_2].add_neighbour(node_1)
            self.nodes[node_1].add_neighbour(node_2)

    def get_edge_key(self, node_1, node_2):
        return 'f{0}-t{1}'.format(node_1, node_2)

    # TODO
    def remove_node(self, node_id):
        if node_id not in self.nodes:
            print('Node {0} does not exists in graph'.format(node_id))
            return
        neighbours = self.nodes[node_id].get_neighbours()
        # for neighbour in neighbours:

    # TODO
    def remove_edge(self, node_1, node_2):
        print('TODO')
        return 'TODO'








