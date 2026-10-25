# Scan every cell of the grid, row by row.
# When you find land that isn’t visited yet, that’s a new island: add 1 to count, mark the cell, and call dfs.
# dfs spreads from that cell through all connected land (up, down, left, right), marking each cell as it goes, so the scan never counts that island again.


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0

        def dfs(r, c):
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #change in direction to move
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols: #the new neighbour you would move to

                    if grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    visited.add((r, c))
                    count += 1
                    dfs(r, c)
        return count