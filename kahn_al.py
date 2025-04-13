from collections import deque
from typing import List,Dict,Set
from graph_al import Graph_al

class Kahn_sort:
    def __init__(self, graph: Graph_al):
        self.graph = graph

    def topological_sort(self) -> List[int]:
        indegree: Dict[int, int] = self.graph.get_indegrees()
        queue = deque([v for v in self.graph.adj_list if indegree[v] == 0])
        result: List[int] = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in self.graph.adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(result) != self.graph.num_vertices:
            raise ValueError("Graf zawiera cykl.") 
    
        return result
        