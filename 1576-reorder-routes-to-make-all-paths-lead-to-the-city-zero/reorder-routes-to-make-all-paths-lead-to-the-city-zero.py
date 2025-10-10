from collections import defaultdict, deque
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # adjacency (undirected for traversal)
        neighbors = defaultdict(list)
        # remember original directed edges
        directed = set()

        for u, v in connections:
            neighbors[u].append(v)
            neighbors[v].append(u)
            directed.add((u, v))  # edge is u -> v in the input

        reverse = 0
        visited = set([0])
        q = deque([0])

        while q:
            city = q.popleft()
            for nei in neighbors[city]:
                if nei in visited:
                    continue
                visited.add(nei)
                # if the original direction is city -> nei, it must be reversed
                if (city, nei) in directed:
                    reverse += 1
                q.append(nei)

        return reverse
