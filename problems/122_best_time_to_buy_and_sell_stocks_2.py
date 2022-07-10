class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_price = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < cur_price:
                cur_price = prices[i]
            else:
                profit += prices[i] - cur_price
                cur_price = prices[i]

        return profit