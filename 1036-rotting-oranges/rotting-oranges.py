# Your structure, fixed
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        rotten = []

        # count fresh and collect starting rotten
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))

        if fresh == 0:
            return 0  # nothing to rot

        minutes = 0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        # BFS by minutes
        while rotten and fresh > 0:
            minutes += 1
            curr = []
            for r, c in rotten:
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        curr.append((nr, nc))
            rotten = curr  # <-- move AFTER finishing the whole minute

        return minutes if fresh == 0 else -1
