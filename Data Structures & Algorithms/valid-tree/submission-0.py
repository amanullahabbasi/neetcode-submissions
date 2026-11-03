from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a tree with n nodes has exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # build the undirected graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # BFS from node 0
        visited = {0}
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for nxt in graph[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        # connected if we reached every node
        return len(visited) == n