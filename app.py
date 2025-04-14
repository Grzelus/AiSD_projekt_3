from graph_al import Graph_al
from tarjan_al import Tarjan_sort
from kahn_al import Kahn_sort
from kahn_nm import KahneAlgorithm_NM
from tarjan_nm import TarjanAlgorithm_NM
from graph_nm import createNeighbourhoodMatrix
import time

def from_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines

def graph_al_from_file(filename):
    lines=from_file(filename)
    num_vertices, num_edges = map(int, lines[0].split())

    graph = Graph_al(num_vertices)

    for line in lines[1:]:
        u, v = map(int, line.split())
        graph.add_edge(u, v)
    return graph

def graph_nm_from_file(filename):
    lines=from_file(filename)
    return createNeighbourhoodMatrix(lines)


print("wybierz format grafu:\n")
print("1) lista sąsiedztwa\n")
print("2) lista następników\n")

format = int(input())

if format == 1:
    file = input("wczytaj graf z pliku: ")
    [graph,Vertices,cycle] = graph_nm_from_file(file)
    if cycle:
        print("graf zawiera cykl.")
        exit()
    print("wybór algorytmu:\n")
    print("1) Kahn\n")
    print("2) Tarjan\n")
    alg = int(input())
    if alg == 1:
        start = time.time()
        kahn = KahneAlgorithm_NM(graph,Vertices)
        end = time.time()
        print(kahn)
    if alg == 2:
        startVertice=input("wybierz wierzchołek z którego chcesz zacząć (domyślnie - Enter):")
        if(startVertice==""):
            startVertice=1
        start = time.time()
        tarjan = TarjanAlgorithm_NM(graph,Vertices,int(startVertice))
        end = time.time()
        print(tarjan)

elif format == 2:
    file = input("wczytaj graf z pliku: ")
    graph = graph_al_from_file(file)
    print("wybór algorytmu:\n")
    print("1) kahn\n")
    print("2) tarjan\n")
    alg = int(input())
    if alg == 1:
        kahn = Kahn_sort(graph)
        if kahn.graph.has_cycle():
            print("graf zawiera cykl.")
            exit()
        start = time.time()
        result = kahn.topological_sort()
        print(result)
        end = time.time()
    elif alg == 2:
        tarjan = Tarjan_sort(graph)
        if tarjan.graph.has_cycle():
            print("graf zawiera cykl.")
            exit()
        

        vertex = input("wybierz wierzchołek z którego chcesz zacząć (domyślnie - Enter): ")

        start = time.time()
        if vertex.strip():
            result = tarjan.topological_sort([int(vertex)])
        else:
            result = tarjan.topological_sort()

        print(result)
        end = time.time()
        
    else:
        print("wybierz poprawną konfigurację.")
        exit()
    print(f"Czas wykonania algorytmu: {start-end}")
