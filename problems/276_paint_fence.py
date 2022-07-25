class Solution:
    def numWays(self, n: int, k: int) -> int:
        dp = [[0 for _ in range(4)] for _ in range(n + 1)]
        #dp[i][j] : the number of cases that i-th fence is painted with the same color for j consecutive fences

        dp[1][1] = k
        for i in range(1, n):
            for j in range(1, 3):
                # current fence is painted with different color from previous fence
                dp[i + 1][1] += dp[i][j] * (k - 1)

                # current fence is painted with same color as previous fence
                dp[i + 1][j + 1] += dp[i][j]

        ans = dp[n][1] + dp[n][2]
        return ans