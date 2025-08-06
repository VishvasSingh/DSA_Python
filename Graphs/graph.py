class Graph:
    def __init__(self):
        self.adj_list = dict()

    def add_vertex(self, vertex) -> bool:
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = list()
            return True

        return False

    def add_edge(self, v1, v2) -> bool:
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True

        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)

            except ValueError:
                pass

            return True

        return False

    def remove_vertex(self, vertex) -> bool:
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True

        return False

    def print_graph(self):
        for vertex, value in self.adj_list.items():
            print(vertex, ' : ', value)


if __name__ == '__main__':
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')

    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('A', 'D')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')

    g.print_graph()

    g.remove_vertex('D')
    print("###########\n")
    g.print_graph()