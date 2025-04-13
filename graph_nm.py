##wypisanie dowolnego grafu
def printGraph(Tab):
    for i in Tab:
        print(i)

## tworzenie macierzy sąsiadującej i listy dostępnych wierzchołków
def createNeighbourhoodMatrix(Tab):
    A=int(Tab[0][0])
    V=int(Tab[0][1])
    AvailableVertices=[]
    for i in range(1,A+1):
        AvailableVertices.append(i)
    Graph=[[0 for x in range(A+1)]for y in range(A+1)]
    for i in range(1,V+1):
        a=int(Tab[i][0])
        b=int(Tab[i][1])
        if(a<=A and b<=A):
            Graph[a][b]=1 
            Graph[b][a]=-1
        else:
            print(f"Out of range {a} and {b}")
    printGraph(Graph)

    return [Graph,AvailableVertices]