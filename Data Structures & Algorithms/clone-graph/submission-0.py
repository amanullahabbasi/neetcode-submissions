"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        copies = {node: Node(node.val)}
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            for nxt in cur.neighbors:
                if nxt not in copies:
                    copies[nxt] = Node(nxt.val)
                    queue.append(nxt)
                copies[cur].neighbors.append(copies[nxt])
        return copies[node]