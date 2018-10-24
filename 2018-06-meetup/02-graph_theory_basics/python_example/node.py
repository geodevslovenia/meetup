class Node:

    def __init__(self, value):
        self.id = value
        self.neighbors = {}

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_neighbours(self):
        return self.neighbors

    def add_neighbour(self, node):
        self.neighbors[node] = node

    def remove_neighbour(self, node):
        if self.neighbors[node]:
            del self.neighbors[node]

    def adjacent(self, node):
        return self.neighbors[node]
