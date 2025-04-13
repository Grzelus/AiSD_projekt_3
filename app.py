from graph_al import Graph_al
from tarjan_sort import Tarjan_sort
from kahn_al import Kahn_sort
from kahn_nm import KahneAlgorithm_NM
from kahn_nm import searchOfZeroVertice_NM
from tarjan_nm import TarjanAlgorithm_NM
from tarjan_nm import FindChild
from tarjan_nm import FindFather
from graph_nm import createNeighbourhoodMatrix
import time

def graph_al_from_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        num_vertices, num_edges = map(int, lines[0].split())

        graph = Graph_al(num_vertices)

        for line in lines[1:]:
            u, v = map(int, line.split())
            graph.add_edge(u, v)

    return graph


print("wybierz format grafu:\n")
print("1) lista sąsiedztwa\n")
print("2) lista następników\n")

format = int(input())

if format == 1:
    print("todo") #todo
elif format == 2:
    file = input("wczytaj graf z pliku: ")
    graph = graph_al_from_file(file)
    print("wybór algorytmu:\n")
    print("kahn\n")
    print("tarjan\n")
    alg = int(input())
    if alg == 1:
        kahn = Kahn_sort(graph)
        start = time.time()
        result = kahn.topological_sort()
        print(result)
        end = time.time()
    if alg == 2:
        tarjan = Tarjan_sort(graph)
        start = time.time()
        result = tarjan.topological_sort()
        print(result)
        end = time.time()
        

