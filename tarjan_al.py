from graph_al import Graph_al
from typing import List, Set

class Tarjan_sort:
    def __init__(self, graph: Graph_al):
        self.graph = graph
        self.visited: Set[int] = set()
        self.rec_stack: Set[int] = set()
        self.result: List[int] = []

    def dfs(self, node: int):
        if self.graph.has_circle:
            return
        
        self.visited.add(node)
        self.rec_stack.add(node)

        for neighbor in self.graph.adj_list[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor)
            elif neighbor in self.rec_stack:
                self.graph.has_circle = True
                return
            
        self.rec_stack.remove(node)
        self.result.append(node)
                
    def topological_sort(self, start_nodes: List[int] = None) -> List[int]:
        if start_nodes is None:
            start_nodes = list(self.graph.adj_list.keys())

        for node in start_nodes:
            if node not in self.visited:
                self.dfs(node)

        if self.graph.has_circle:
            raise ValueError("Graf zawiera cykl.")
        
        return self.result[::-1]
