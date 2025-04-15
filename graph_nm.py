from typing import Dict, List

##wypisanie dowolnego grafu
def printGraph(Tab):
    for i in Tab:
        print(i)
##szukanie cyklu
def has_cycle(Graph):
    n = len(Graph)
    visited = [0] * n 

    def dfs(start):
        current = start
        visited[current] = 1
        for v in range(n):
            if Graph[current][v] == 1:
                if visited[v] == 1:
                    return True
                if visited[v] == 0:
                    if dfs(v):
                        return True
        visited[current] = 2
        return False

    for node in range(n):
        if visited[node] == 0:
            if dfs(node):
                return True

    return False

## tworzenie macierzy sąsiadującej i listy dostępnych wierzchołków
def createNeighbourhoodMatrix(Tab):
    A,V=map(int,Tab[0].split())
    AvailableVertices=[]
    for i in range(1,A+1):
        AvailableVertices.append(i)

    Graph=[[0 for x in range(A+1)]for y in range(A+1)]
    
    for i in range(1,V+1):
        a,b=map(int,Tab[i].split())
        if(a<=A and b<=A):
            Graph[a][b]=1 
            Graph[b][a]=-1
        else:
            print(f"Out of range {a} and {b}")
        cycle=has_cycle(Graph)

    printGraph(Graph)
    return [Graph,AvailableVertices,cycle]