class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_val = prices[0]
        for price in prices:
            if price <= lowest_val:
                lowest_val = price
            else:
                max_profit = max(max_profit, price - lowest_val)
        return max_profit
                

        