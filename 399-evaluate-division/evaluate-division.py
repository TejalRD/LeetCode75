class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build a weighted graph: g[u][v] = u / v
        g = defaultdict(dict)
        for (a, b), k in zip(equations, values):
            g[a][b] = k
            g[b][a] = 1.0 / k

        def evaluate(src: str, dst: str) -> float:
            # If either variable is unseen, no answer
            if src not in g or dst not in g:
                return -1.0
            # Trivial self-division
            if src == dst:
                return 1.0

            # BFS carrying running product from src to dst
            q = deque([(src, 1.0)])
            seen = {src}
            while q:
                node, prod = q.popleft()
                if node == dst:
                    return prod
                for nei, w in g[node].items():  # node/nei = w
                    if nei not in seen:
                        seen.add(nei)
                        q.append((nei, prod * w))
            return -1.0

        return [evaluate(c, d) for c, d in queries]