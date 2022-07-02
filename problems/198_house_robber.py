class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        # For corner case
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]

        dp = [0] * (n + 1)
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]