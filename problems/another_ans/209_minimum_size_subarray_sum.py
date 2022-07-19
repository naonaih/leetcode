class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        INF = 10 ** 6

        n = len(nums)
        l = 0
        s = 0

        ans = INF

        for r in range(n):
            s += nums[r]
            while s >= target:
                print(r, l)
                ans = min(ans, r - l + 1)
                s -= nums[l]
                l += 1

        if ans == INF:
            ans = 0

        return ans
