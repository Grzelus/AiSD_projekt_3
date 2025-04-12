from typing import Dict, List

class Graph_al:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj_list: Dict[int, List[int]] = {i: [] for i in range(i, num_vertices + 1)}

    def add_edge(self, u: int, v: int):
        self.adj_list[u].append(v)

    def get_indegrees(self) -> Dict[int, int]:
        indegrees = {i: 0 for i in range(1, self.num_vertices + 1)}
        for u in self.adj_list:
            for v in self.adj_list[u]:
                indegrees[v] += 1
        return indegrees
        