from typing import Dict, List


def FindChild(Graph,AvaliableVertices,current,color):
    for i in range(1,len(AvaliableVertices)):
        if Graph[current][i]==1 and AvaliableVertices[i]==color:
            return i
    return 0
def FindFather(Graph,AvaliableVertices,current,color):
    for i in range(1,len(AvaliableVertices)):
        if Graph[current][i]==-1 and AvaliableVertices[i]==color:
            return i
    return 0

def TarjanAlgorithm_NM(Graph, Vertices,startingVertice):
    AvaliableVertices=["white" for x in range(len(Vertices)+1)]
    currentVertice=startingVertice
    AvaliableVertices[startingVertice]="grey"
    listOfSorted=[]
    while 1:
        i=FindChild(Graph,AvaliableVertices,currentVertice,"white")
        while i!=0:
            AvaliableVertices[i]="grey" 
            currentVertice=i
            i=FindChild(Graph,AvaliableVertices,currentVertice,"white")
        AvaliableVertices[currentVertice]="black"
        listOfSorted.insert(0,currentVertice)
        currentVertice=FindFather(Graph,AvaliableVertices,currentVertice,"grey")
        if not currentVertice: 
            for i in range(1, len(AvaliableVertices)):
                if(AvaliableVertices[i]=="white"):
                    currentVertice=i
                    break
            if not currentVertice:
                break
    return listOfSorted 
