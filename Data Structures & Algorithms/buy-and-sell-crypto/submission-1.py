class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof=0
        if len(prices)==0:
            return 0
        cur_min=prices[0]
        for i in range(1,len(prices)):
            cur_prof=max(0,prices[i]-cur_min)
            max_prof= max(cur_prof ,max_prof)
            cur_min= min(cur_min,prices[i])
        
        return max_prof
        