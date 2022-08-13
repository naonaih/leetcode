class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 10 ** 9
        # dp[i] : the number of total coins to compose amount
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for i in range(len(coins)):
            for j in range(amount + 1):
                if j - coins[i] < 0:
                    continue
                dp[j] = min(dp[j - coins[i]] + 1, dp[j])

        if dp[amount] == INF:
            return -1
        else:
            return dp[amount]