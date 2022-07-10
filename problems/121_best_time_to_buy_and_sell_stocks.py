class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10 ** 5
        ans = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            ans = max(ans, prices[i] - min_price)

        return ans
