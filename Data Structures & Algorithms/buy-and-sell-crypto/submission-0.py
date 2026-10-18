class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_to_i=prices[0]
        for i in range(1,len(prices)):
            min_to_i= min(min_to_i,prices[i-1])
            cur_profit= max(0,prices[i]-min_to_i)
            if cur_profit>max_profit:
                max_profit=cur_profit
        return max_profit

        
        