class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prince = float('inf')
        profit = 0
        for price in prices:
            if price < min_prince:
                min_prince = price
            else:
                profit = max(price - min_prince, profit)

        return profit