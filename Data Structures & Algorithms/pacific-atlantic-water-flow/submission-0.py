class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, seen):
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                        seen.add((nr, nc))
                        dfs(nr, nc, seen)

        for r in range(rows):
            pacific.add((r, 0)) #pacific starts at left column
            dfs(r, 0, pacific)
            atlantic.add((r, cols-1))
            dfs(r, cols - 1, atlantic)
        for c in range(cols):
            pacific.add((0, c))
            dfs( 0 , c, pacific)
            atlantic.add((rows - 1, c))
            dfs(rows - 1, c, atlantic)

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        return result