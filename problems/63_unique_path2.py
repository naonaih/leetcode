class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [[0 for _ in range(m)] for _ in range(n)]

        # starting cell has obstacle, we have no ways
        if obstacleGrid[0][0] == 1:
            dp[0][0] = 0
        # Number of ways of reaching the starting cell = 1.
        else:
            dp[0][0] = 1

        # Filling the values for the first row
        for x in range(1, m):
            if obstacleGrid[0][x] == 1:
                dp[0][x] = 0
            else:
                dp[0][x] = dp[0][x - 1]

        # Filling the values for the first column
        for y in range(1, n):
            if obstacleGrid[y][0] == 1:
                dp[y][0] = 0
            else:
                dp[y][0] = dp[y - 1][0]

        # Starts filling from cell(1,1). If a cell has an obstacle, the ways of reaching the cell should be 0.
        for y in range(1, n):
            for x in range(1, m):
                if obstacleGrid[y][x] == 1:
                    dp[y][x] = 0
                else:
                    dp[y][x] += dp[y][x - 1]
                    dp[y][x] += dp[y - 1][x]

        return dp[n - 1][m - 1]