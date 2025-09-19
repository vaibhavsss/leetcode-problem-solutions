class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #solving this using bfs
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            queue=[(r, c)]
            visited.add((r, c))

            while queue:
                row, col = queue.pop(0)
                for nr, nc in [(row-1, col), (row, col+1), (row+1, col), (row, col-1)]:
                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc]=="1" and
                        (nr, nc) not in visited):
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands