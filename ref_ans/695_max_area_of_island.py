class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            # base case
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r,c) in visit:
                return 0

            # add current cell into visit lists
            visit.add((r, c))

            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)


        area = 0

        # starts dfs from each of cells
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))

        return area