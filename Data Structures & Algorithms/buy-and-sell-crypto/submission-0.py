class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0                    # Buy day
        max_profit = 0

        for right in range(len(prices)):   # Sell day

            # Found a cheaper day to buy
            if prices[right] < prices[left]:
                left = right

            else:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)

        return max_profit