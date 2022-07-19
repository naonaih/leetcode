class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        INF = 10 ** 6

        n = len(nums)
        l = 0
        r = 0
        s = nums[0]
        if s >= target:
            return 1

        ans = INF

        while r < n - 1:
            # expand right side
            while r < n - 1:
                r += 1
                s += nums[r]
                if s >= target:
                    ans = min(ans, r - l + 1)
                    break

            print(r)
            # shrink left side
            while l <= r:
                l += 1
                s -= nums[l - 1]
                if s >= target:
                    ans = min(ans, r - l + 1)
                else:
                    break

        if ans == INF:
            ans = 0

        return ans
