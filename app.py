from graph_al import Graph_al
from tarjan_sort import Tarjan_sort
from kahn_al import Kahn_sort

def graph_al_from_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        num_vertices, num_edges = map(int, lines[0].split())

        graph = Graph_al(num_vertices)

        for line in lines[1:]:
            u, v = map(int, line.split())
            graph.add_edge(u, v)

    return graph

graph = graph_al_from_file("test.txt")


tarjan = Tarjan_sort(graph)
print(tarjan.topological_sort())
