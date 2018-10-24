class Edge:

    def __init__(self, node1, node2, value):
        self.nodes = {'from': node1, 'to': node2}
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_connected(self):
        return self.nodes




