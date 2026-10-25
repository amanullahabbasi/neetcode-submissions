class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        count = 0

        def dfs(node):
            for nxt in graph[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    dfs(nxt)

        for node in range(n):
            if node not in visited:
                visited.add(node)
                count += 1
                dfs(node)
        return count