from typing import Dict,Set,List

class Graph_al:
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj_list: Dict[int, List[int]] = {i: [] for i in range(1, num_vertices + 1)}

    def add_edge(self, u: int, v: int):
        self.adj_list[u].append(v)

    def get_indegrees(self) -> Dict[int, int]:
        indegrees = {i: 0 for i in range(1, self.num_vertices + 1)}
        for u in self.adj_list:
            for v in self.adj_list[u]:
                indegrees[v] += 1
        return indegrees
        
    def has_circle(self) -> bool:
        visited: Set[int] = set()
        rec_stack: Set[int] = set()

        def dfs(node: int) -> bool:
            visited.add(node)
            rec_stack.add(node)

            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True  
            rec_stack.remove(node)
            return False

        for node in self.adj_list:
            if node not in visited:
                if dfs(node):
                    return True

        return False