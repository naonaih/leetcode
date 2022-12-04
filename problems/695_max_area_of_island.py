class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Y = len(grid)
        X = len(grid[0])

        is_visit = [[False for _ in range(X)] for _ in range(Y)]

        def dfs(y, x):
            if is_visit(y, x):
                return
            else:
                is_visit(y, x)

            if x + 1 < X:
                dfs(y, x + 1)
            if y + 1 < Y:
                dfs(y + 1, x)

        ans = 0
        for i in range(Y):
            for j in range(X):
                if is_visit[i][j]:
                    continue
                else:
                    ans += 1
                    dfs(i, j)
        return ans
