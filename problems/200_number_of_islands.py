class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        chk = [[False for _ in range(n)] for _ in range(m)]

        def dfs(x, y):
            if chk[y][x]:
                return
            chk[y][x] = True

            if grid[y][x] == '0':
                return

            if x + 1 < n:
                dfs(x + 1, y)
            if x - 1 >= 0:
                dfs(x - 1, y)
            if y + 1 < m:
                dfs(x, y + 1)
            if y - 1 >= 0:
                dfs(x, y - 1)

        ans = 0
        for y in range(m):
            for x in range(n):
                if chk[y][x] == False and grid[y][x] == "1":
                    ans += 1
                    dfs(x, y)
        return ans