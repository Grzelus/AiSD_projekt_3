
## znajdowanie wierzchołka o zerowym wejściu (macierz sąsiedztwa)
def searchOfZeroVertice_NM(Graph,AvailableVertices):
    for i in AvailableVertices:
        mini=0
        for j in AvailableVertices:
            mini=min(mini,Graph[i][j])
        if not mini:
            return i
    return None
## algorythm kahna (macierz sąsiedztwa)           
def KahneAlgorithm_NM(Graph,Vertices):
    AvailableVertices=Vertices
    ListOfvertices=[]
    while(len(AvailableVertices)):
        a = searchOfZeroVertice_NM(Graph,AvailableVertices)
        if a:
            ListOfvertices.append(a)
            AvailableVertices.remove(a)
    return ListOfvertices