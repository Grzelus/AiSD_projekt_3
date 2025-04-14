from typing import List, Set
from graph_al import Graph_al

class Tarjan_sort:
    def __init__(self, graph: Graph_al):
        self.graph = graph
        self.visited: Set[int] = set()
        self.rec_stack: Set[int] = set()
        self.result: List[int] = []

    def dfs(self, node: int):
        self.visited.add(node)
        self.rec_stack.add(node)

        for neighbor in self.graph.adj_list[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor)

        self.rec_stack.remove(node)
        self.result.append(node)
                
    def topological_sort(self, start_nodes: List[int] = None) -> List[int]:
        if self.graph.has_cycle():
            raise ValueError("Graf zawiera cykl.")

        if start_nodes is None:
            start_nodes = list(self.graph.adj_list.keys())

        for node in start_nodes:
            if node not in self.visited:
                self.dfs(node)

        return self.result[::-1]
