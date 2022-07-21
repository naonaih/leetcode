class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [[0 for _ in range(n)] for _ in range(2)]
        # in case that robber did not rob from 1st house
        dp[0][0] = 0
        # in case that robber robbed from 1st house
        dp[1][0] = nums[0]

        for i in range(1, n - 1):
            dp[0][i] = max(dp[0][i - 2] + nums[i], dp[0][i - 1])
            dp[1][i] = max(dp[1][i - 2] + nums[i], dp[1][i - 1])

        dp[0][n - 1] = max(dp[0][n - 3] + nums[n - 1], dp[0][n - 2])
        dp[1][n - 1] = dp[1][n - 2]

        return max(dp[0][n - 1], dp[1][n - 1])