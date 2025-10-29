class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0]      # profit when holding a stock
        cash = 0               # profit when not holding a stock
        
        for p in prices[1:]:
            # Either keep holding, or buy today (spend cash)
            hold = max(hold, cash - p)
            # Either keep cash, or sell today (pay fee)
            cash = max(cash, hold + p - fee)
        
        return cash

        